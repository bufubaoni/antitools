# web 异步协同爬虫
原文[地址](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html)
作者:
- A. Jesse Jiryu Davis(美国MongoDB 工程师，MongoDB 的py驱动的作者，主导mongoDB的c驱动)
- Guido van Rossum (不说了)

## 介绍
经典计算机理论强调高效率的算法，尽可能快速的完成计算。但是大多数的网络相关时间瓶颈并没有在计算上，打开较慢的连接，或者不频繁的事件。此项目目标：提高网络爬虫效率，当前处理方法是使用异步 i/o 或者 “异步”。

此章节建立一个简单的web 爬虫，爬虫的原型为异步应用因为要等待诸多相应，仅仅做少量计算。一次获取的页面越多，计算完成的就越快。如果每个请求都分配一个线程，则随着并发请求的增加，它将耗尽内存或者其他线程的资源，直到耗尽 sockets，通过使用异步i/o避免了线程的开销。

我们迭代了三次完成这个项目

- 第一次，做一个异步事件轮询，并写一个带有回调事件循环的爬虫，这样做的效率很高，但带来的是扩展性和复杂度将会导致无法扩展和维护的代码。
- 第二次，使用python的协程，可以同时达到效率和扩展性，我们实现了简单的协程在python中使用生成器方法。
- 第三次，我们使用标准库的异步和协程的全部特性，当然需要异步队列来实现调度。

## 任务
一个web爬虫爬取和下载网站的所有页面，或者保存其中的内容。从根url开始，获取每个页面，解析页面的连接到其他页面，然后将这些添加到队列中。直到没有页面可爬取的时候停止此时队列为空。
我们可以同时下载许多页面来加速这个过程。一旦爬虫爬取了新的连接，他会单独的使用socket获取新页面提取其中内容，当此相应完成后则开始解析，并添加新的连接给请求队列。可能会出现无响应的情况当，在高并发中会降低性能，因此我们应当降低并发的数量，并将其余链接保留在队列中，直到之前的请求完成。

## 旧方法
如何实现爬虫并发。一般来说，我们将建立一个线程池。每一个线程都会t哦那个过socket下载一个页面，例如我们下载一个页面从*xkcd.com*。

```python
def fetch(url):
    sock = socket.socket()
    sock.connect(('xkcd.com', 80))
    request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    # Page is now downloaded.
    links = parse_links(response)
    q.add(links)
```
通常，socket 的操作为空，当线程调用方法 *connect* 或者 *recv*,会暂停直到操作完成。为了一次下载多个页面，我们需要多线程。
一个复杂的应用通过将空闲的线程保留在线程池中，然后再对其复用，来降低线程创建的消耗，socket同样适用连接池。

当然，线程的代价是昂贵的，并且操作系统对进程，用户，和机器有着各种各样的限制。在Jesse's 的系统，一个py的线程将占用50k的内存，启用1w以上的线程将导致程序的失败。如果我们并发的操作数以万计的socket，我们就将耗尽线程。每个线程的开销或者系统对线程的限制都将是瓶颈。

在他的文章的一开始["The C10K problem"](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html#fn3)中，Dan Kegel 他阐述了多线程的i/o的局限性。
> It's time for web servers to handle ten thousand clients simultaneously, don't you think? After all, the web is a big place now.

> 这是一个并发万计的时代，你不认为吗？因为web大有可为。

Kegel 创建了 "C10K" 在1999年。万计的连接听上去很不错，问题的改变只是量上的而非质变。回到之前，使用线程每个链接对于C10K都是不切实际的。现在的容器更为高级。确实，我们的爬虫可以使用线程工作的很好。但是面对巨大规模的应用，例如十万级别的连接，面对的问题仍然是，它的规模超过了大多数的系统可以创建的socket，如果不使用多线程，将如何实现呢？

## 异步

异步i/o框架在一个单线程上使用非阻塞socket并行执行。使用异步爬虫，我们在使用socket连接服务之前，设置其为非阻塞：

```python
sock = socket.socket()
sock.setblocking(False)
try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass
```
一个非阻塞的socket当*connect*的时候会触发异常，这个异常只是重现底层c的一个方法，这个方法将*errno*设置为*EINPROGRESS*告知方法开始。

所以说爬虫应当知道连接何时开始，以发送http 请求，我们使用一个简单的循环来发送请求：

```python
request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(url)
encoded = request.encode('ascii')

while True:
    try:
        sock.send(encoded)
        break  # Done.
    except OSError as e:
        pass

print('sent')
```
当前方法不仅仅是费电，而且也不能有效的调度的多个socket，在最早的时候，BSD Uinx 的解决方法是*select*,C 方法等待非阻塞socket或者socket的数组。当代的互联网需求面对的是大量的连接应运而生的是如 *poll*,如bsd上的*kqueue*,linux上的*epoll*。这些api和*select*类似，但是解决的更大的连接数。

py3.4的 `DefaultSelector`使用更好的如`select`的方法在系统上。为了注册一个i/o相关的网络通知，我们创建一个非阻塞socket使用默认*select*注册。

```python
from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

sock = socket.socket()
sock.setblocking(False)
try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass

def connected():
    selector.unregister(sock.fileno())
    print('connected!')

selector.register(sock.fileno(), EVENT_WRITE, connected)
```

我们忽略错误需要调用`selector.register`，传递socket的文件描述符和一个常量，来表示我们的等待事件。在连接开始时我们设置`EVENT_WRITE`:我们想知道什么时候socket是可读的，我们仍旧使用`connected`方法，当事件运行的时候调用的方法我们称之为回调函数。

```python
def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()
```
`callback`回调函数存储的是`event_key.data`，一旦监测到非阻塞socket连接的时候就会执行。
不同于第一次实现的循环，调用`select`暂停，等待下一个i/o事件。然后循环等待这些事件轮询执行。
尚未完成的操作将始终保持挂起，直到某个时间循环执行。

我们将演示什么，我们将展示当操作完成后如何操作和执行回掉函数，一个异步框架建立在我们展示的两个功能之上-非阻塞socket和事件循环-在单线程上运行并发操作。

我们在这里实现了“并发”，但是并非传统意义上的“并行”。我们建立了一个小型的重叠的i/o系统，当其他操作还在执行的时候可以开启一个新的操作。他并不是利用多核执行并行计算。但是这个系统是为了解决i/o绑定问题的，而不是cpu限制的。

所以我们这个事件循环对于并发i/o更为有效率，因为他不会每个链接都占用线程资源。但是在我们继续之前，重要的是纠正一个常见的错误-异步快于多线程。通常并非如此，的确在py中象我们这样的事件事件在少量的非常活跃的服务连接是慢于多线程的，在没有全局解释器所的情况下，线程能够在这样的工作负载下表现的很好。如果应用的瓶颈在于阻塞和休眠的连接，这样情况下，异步i/o是相当正确的。

## 回调函数
我们已经构建了可运行的异步框架，接下来建立web爬虫。一个简单的url提取器写起来也是很痛苦的

我们从设置一个没有爬取的全局url集合开始，和一个已经爬取的集合。

```python
urls_todo = set(['/'])
seen_urls = set(['/'])
```
`seen_urls`包含`urls_todo`加上完整的url。这两个集合初始化自根url“/”

提取页面内容需要一些列的回掉函数。当socket连接后`connected`将被调用，然后向服务器发送一个 GET 请求。但是它必须等待 响应。如果，回调触发的时候，不能读取完整的响应，它将再次触发，知道读取所有的内容。

我们集中这些回调函数到`Fetch`object中。它需要一个 url，一个socket，和一个字节型的缓存区。

```python
class Fetcher:
    def __init__(self, url):
        self.response = b''  # Empty array of bytes.
        self.url = url
        self.sock = None
```
从调用 `Fetcher.fetch`开始：

```python
    # Method on Fetcher class.
    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass

        # Register next callback.
        selector.register(self.sock.fileno(),
                          EVENT_WRITE,
                          self.connected)
```
`fetch` 方法开始连接一个socket，但是应当在通讯前通知。它必须返回一个事件循环的控制器来等待连接。为了便于理解，想象一个整个应用是这个样子的：

```python
# Begin fetching http://xkcd.com/353/
fetcher = Fetcher('/353/')
fetcher.fetch()

while True:
    events = selector.select()
    for event_key, event_mask in events:
        callback = event_key.data
        callback(event_key, event_mask)
```
所有的事件通知在进程调用`select`时候调用，因此`fetch`必须手动控制时间循环，以便知道socket合适连接。只有这样循环中才能执行上边`fetch`结尾处注册的回调函数。

下面是`connected`的实现

```python
# Method on Fetcher class.
def connected(self, key, mask):
    print('connected!')
    selector.unregister(key.fd)
    request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
    self.sock.send(request.encode('ascii'))

    # Register the next callback.
    selector.register(key.fd,
                        EVENT_READ,
                        self.read_response)
```
这个方法发送一个`GET`请求。真正的应用会监测`send`的返回值一方整个信息不能立即发送。以为我们的请求和应用都很小。当调用`send`方法的时候，等待响应。当然，他必须注册另一个回调，并放弃对事件循环的控制。下一个和最后一个回调，`read_response`处理服务器的回复：

```python
    # Method on Fetcher class.
    def read_response(self, key, mask):
        global stopped

        chunk = self.sock.recv(4096)  # 4k chunk size.
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)  # Done reading.
            links = self.parse_links()

            # Python set-logic:
            for link in links.difference(seen_urls):
                urls_todo.add(link)
                Fetcher(link).fetch()  # <- New Fetcher.

            seen_urls.update(links)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True
```
selector监测socket为"readable"时回调函数将被执行，这意味着两件事情，socket已经有了数据或者socket已经关闭。

回掉将会请求4kb的数据。如果比读取的少，`chunk`包括所有的数据，如果多余这些数据，`chunk`将回事4kb的数据，然后socket仍然可读，事件循环将会在下一个tick时再一次执行回调。当响应完成，服务器将会关闭socket然后`chunk`清空。

`parse_links`方法，未列出，返回url的集合。我们没有上限的为每一个新的url开启一个抓取器。注意一个优点异步回调：我们不需要围绕共享数据而互斥，例如当我们添加向`seen_urls`集合中添加数据的时候。不会有多任务的抢占，这种模式下我们不能在自己的代码任意位置被打断。

我们添加全局方法`stopped`变量，并控制循环。

```python
stopped = False

def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()
```

一旦所有的页面都抓取完毕，那么嗅探器捡回停止所有的全局循环，并退出程序

这个简单的实例提现了异步代码的维护困难。我们需要一定的途径来表现一系列的计算和i/o操作，和调度多个这样的操作并发运行。但是除了多线程之外，一系列的操作无法被收集到单个函数：然而一个方法开始一个i/o 操作，它将明确的保存未来的状态，如果他又返回值。请自己思考并编写这个节省状态的代码。

解释一下为什么做这些，思考一下我们怎么在一个阻塞线程获取url

```python
# Blocking version.
def fetch(url):
    sock = socket.socket()
    sock.connect(('xkcd.com', 80))
    request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    # Page is now downloaded.
    links = parse_links(response)
    q.add(links)
```

这个函数将记录两个socket的操作间的状态。当一个url发送socket的时候相应。当函数在线程上运行时使用语言的最基本的局部变量来存储临时状态在栈中。函数当然有一个 "continuation",代码计划在i/o完成后执行的代码。运行时通过存储线程的指令指针保存运行状态。你不必考虑回复这些局部变量和i/o的后续。踏实语言内置的。

但是在基于回调的异步框架中，这些语言特性是没有帮助的。当等待i/o的时候，这个函数必须明确存储他自己的状态，因为函数在i/o完成之前会丢失他的堆栈帧。为了代替局部变量，我们的基于回掉的例子将存储 `sock`和`response`作为 `self`的`attributes`,在`Fetcher`的实例中，代替指令指针，它通过注册链接的回调和`read_response`来存储接下来的流程。随着应用规模的增长，我们在回回调中手动保存的状态的复杂性也在增加。这样的繁重的记录使得编程工作很头痛。

更甚，当回掉发生错误抛出异常，在它和下一个回掉发生之间？也就是我们的`parse_links` 方法他抛出异常如下：

```python
Traceback (most recent call last):
  File "loop-with-callbacks.py", line 111, in <module>
    loop()
  File "loop-with-callbacks.py", line 106, in loop
    callback(event_key, event_mask)
  File "loop-with-callbacks.py", line 51, in read_response
    links = self.parse_links()
  File "loop-with-callbacks.py", line 67, in parse_links
    raise Exception('parse error')
Exception: parse error
```

堆栈信息仅仅显示时间循环运行了回调。并没有记录什么导致的异常。当异常抛出的时候有两件事情发生了，我们没有记录异常，导致我们从哪里来到哪里去都丢失了，这种上下文的丢失叫做"stack ripping"(堆栈翻录)，并且许多情况下他混淆了程序员。"stack ripping" 还阻止为我们为回掉函数安装异常处理程序，如"try except" 块来包装回掉函数和他以及其后代树

因此除了关于多线程和异步的相对效率的长期争论意外还有另一个争论是更容易犯错的：如果你错误的同步他们，线程就容易受到数据竞争，但是回调时由于"stack ripping"的存在而调试受限。


## 协程
一个诱人的承诺，可以编写异步代码，将毁掉的效率与传统的多线程结合起来。这种组合称谓`coroutines`协程，使用py3.4的标准的 asyncio 库和一个 "aiohttp"的包，在协程中直接获取url。

```python
    @asyncio.coroutine
    def fetch(self, url):
        response = yield from self.session.get(url)
        body = yield from response.read()
```
他也是可扩展的，对比与50k的线程消耗的内存和操作系统对线程的限制，一个py的协程任务在 Jesse 的系统上只占用3k的内存。python 可以轻松的开启数十万的协程。

协程的概念，可以追溯到计算机科学的起初，很简单：他是一个可以暂停和恢复的子程序。而线程是由操作系统抢占式多任务，协同是多任务协作：他们选择何时停止，以及何时运行下一个。

有很多协程的实现，即使在py中也有好几个。py3中有一个标准"asyncio"库中协程是基于generators，Future 类和"yield from"语句构建的。从py3.5开始协程作为语言的本身的属性，然而，了解协程，因为他们第一次在py3.4 中实现，使用预先存在的语言工具，是解决py3.5 本地协程的基础。

为了解释py3.4 的基于 generators 协程，我们将介绍一些 generators 和如何在 asyncio 中使用协程，我相信你会喜欢阅读他，就像我们喜欢它一样。一旦我们解释基于 generators的协程程序，我们将在异步web 爬虫中使用它们。

## Python 的 Generators 如何工作
在你掌握 Generator 之前，你必须了解一般情况下python的函数的工作原理。通常，当py函数调用子进程的时候，子例程保留控制，知道返回或者抛出异常，然后控制权交还给调用者：

```python
>>> def foo():
...     bar()
...
>>> def bar():
...     pass
```

python 官方解释器是用C来写的。执行py函数的c函数被称之为 mellifluously,`PyEval_EvalFrameEx`。它需要一个python的栈框架对象，并在框架的上下文中评估py的字节码。这里是`foo`的字节码：

```python
>>> import dis
>>> dis.dis(foo)
  2           0 LOAD_GLOBAL              0 (bar)
              3 CALL_FUNCTION            0 (0 positional, 0 keyword pair)
              6 POP_TOP
              7 LOAD_CONST               0 (None)
             10 RETURN_VALUE
```

`foo`在调用`bar`函数的时候压入函数栈，然后从栈上弹出它的返回值，将 `None`压栈，然后返回`None`。

当 `PyEval_EvalFrameEx` 遇到`CALL_FUNCTION`字节码的时候，他创建一个新的py栈框架和资源：它调用`PyEval_EvalFrameEx`并使用新的资源，这些资源将被用来执行`bar`

了解py堆栈帧在堆内存的分配是很重要的！py的解释器是一个正常的c程序，所以他的堆栈也是正常的堆栈帧。但py操作堆栈帧是在堆上。除此之外，这意味着py的堆栈帧可以超越其函数调用。要以交互的方式查看，请从`bar`内部保存当前帧：

```python
>>> import inspect
>>> frame = None
>>> def foo():
...     bar()
...
>>> def bar():
...     global frame
...     frame = inspect.currentframe()
...
>>> foo()
>>> # The frame was executing the code for 'bar'.
>>> frame.f_code.co_name
'bar'
>>> # Its back pointer refers to the frame for 'foo'.
>>> caller_frame = frame.f_back
>>> caller_frame.f_code.co_name
'foo'
```

![img](http://aosabook.org/en/500L/crawler-images/function-calls.png)

该功能现在设置为py的 generators ，使用相同的构建块-代码兑现和堆栈帧-达到特殊效果。

下面是生成器的函数：

```python
>>> def gen_fn():
...     result = yield 1
...     print('result of yield: {}'.format(result))
...     result2 = yield 2
...     print('result of 2nd yield: {}'.format(result2))
...     return 'done'
...  
```

当py完成`gen_fn`字节码，它执行到`yield`语句然后得知`gen_fn`是一个生成函数，并不是一般的函数。他在内存重打下标志：

```python
>>> # The generator flag is bit position 5.
>>> generator_bit = 1 << 5
>>> bool(gen_fn.__code__.co_flags & generator_bit)
True
```

当调用生成函数的时候，python将会看到生成器标志，他并不返回一个函数，而是创建一个生成器：

```python
>>> gen = gen_fn()
>>> type(gen)
<class 'generator'>
```
python 生成器封装了在栈上加上代码的引用，`gen_fn`的主体：

```python
>>> gen.gi_code.co_name
'gen_fn'
```
从`gen_fn`调用的所有生成器都指向相同的代码。但是每个都有自己的堆栈帧。这个对战帧不存在于任何实际的堆栈，它只是等待调用：

![generators](http://aosabook.org/en/500L/crawler-images/generator.png)

该帧拥有"last instruction"指针（最后指令），它表示最近执行的命令。初始值为-1，表示生成器尚未开始：

```python
>>> gen.gi_frame.f_lasti
-1
```

当我们调用`send`,生成器到达第一个`yield`,然后暂停。`send`的返回值为 1 ，因为传递给`gen`的是一个`yield`表达式。

```python
>>> gen.send(None)
1
```
从开始计算（生成器）生成器的指令为3字节，部分通过编译的python代码为56字节：

```python
>>> gen.gi_frame.f_lasti
3
>>> len(gen.gi_code.co_code)
56
```
生成器可以在任何时候从任何函数回复，因为他的堆栈帧在堆上，而非栈上。它在调用层次结构中的位置不是固定的，并且不遵循常规函数的先进先出顺序。它是自由的，无束缚的。

我们可以给生成器发送"hello"然后它将返回`yield`表达式，生成器会继续执行，直到 `yield 2`:

```python
>>> gen.send('hello')
result of yield: hello
2
```
现在栈上信息包括局部变量`result`:

```python
>>> gen.gi_frame.f_locals
{'result': 'hello'}
```
从`gen_fn`创建的其他的生成器将有自己的堆栈帧和局部变量。

当我们再次调用`send`的时候，生成器继续从他的第二个`yield`,完成之后会抛出`StopIteration`异常。

```python
>>> gen.send('goodbye')
result of 2nd yield: goodbye
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration: done
```
这个异常会有一个返回值"done".

## 使用生成器建立协程
因此生成器可以停止，并且可以使用恢复值，并且它具有返回值。听起来很适合构建异步编程模型，没有意大利面条一样的回调！我们想构建一个"协程"：一个在程序中和其他程序合作（scheduled）的程序。我们的协程将是python的标准库"asyncio"的简化版本。在asyncio我们将使用 generator, futures 和"yield from"语句。

首先我们需要一种表示协程正在等待结果的方法。精简版本：

```python
class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)
```

future事例的初始化为待定，它通过`set_result`来"解析".

```python
class Fetcher:
    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass
        selector.register(self.sock.fileno(),
                          EVENT_WRITE,
                          self.connected)

    def connected(self, key, mask):
        print('connected!')
        # And so on....
```

`fetch`首先连接socket，然后注册了一个回调，`connected`,当socket连接时执行。现在我们可以在一个协程中结合此两步：
```python
    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass

        f = Future()

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(),
                          EVENT_WRITE,
                          on_connected)
        yield f
        selector.unregister(sock.fileno())
        print('connected!')
```
`fetch`是一个生成函数，而不是一个常规的函数，因为他包含`yield`语句。我们创建一个等待的future,yield 会暂停`fetch`直到socket准备完毕。内函数`on_connected`会解析 future.

但是当 future解析完成后，如何恢复生成器呢？我们需要一个协程 驱动。让我们叫他"task":

```python
class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            return

        next_future.add_done_callback(self.step)

# Begin fetching http://xkcd.com/353/
fetcher = Fetcher('/353/')
Task(fetcher.fetch())

loop()
```

task 通过`fetch`会发送`None`来启动生成器，`fetch`会运行到yields，task会捕获`next_future`。当socket连接的时候，事件循环运行回调函数`on_connected`,然后解析future，调用`step`,恢复`fetch`.

## 抓取器协程 `yield from`

一旦socket连接上了，我们会发送 HTTP 的GET 请求然后读取响应内容。这些步骤不会再分散到各个回调中，我们将集中到相同的生成函数中。
```python
    def fetch(self):
        # ... connection logic from above, then:
        sock.send(request.encode('ascii'))

        while True:
            f = Future()

            def on_readable():
                f.set_result(sock.recv(4096))

            selector.register(sock.fileno(),
                              EVENT_READ,
                              on_readable)
            chunk = yield f
            selector.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                # Done reading.
                break
```

这段代码读取socket所有返回信息，看上去很有用。我们如何将它从`fetch` 转换为子程序呢？现在的Py3`yield from`有令人欣喜的特性，他可以将一个generator代理给另一个generator.

该如何做呢？我们先回顾一下那个简单的例子：

```python
>>> def gen_fn():
...     result = yield 1
...     print('result of yield: {}'.format(result))
...     result2 = yield 2
...     print('result of 2nd yield: {}'.format(result2))
...     return 'done'
...   
```

为了从一个generator调用另一个generator,即代理使用`yield from`.

```python
>>> # Generator function:
>>> def caller_fn():
...     gen = gen_fn()
...     rv = yield from gen
...     print('return value of yield-from: {}'
...           .format(rv))
...
>>> # Make a generator from the
>>> # generator function.
>>> caller = caller_fn()
```

`caller`就像是在使用一个生成器，实际上它之前是`gen`，它仅仅是gen的委托：

```python
>>> caller.send(None)
1
>>> caller.gi_frame.f_lasti
15
>>> caller.send('hello')
result of yield: hello
2
>>> caller.gi_frame.f_lasti  # Hasn't advanced.
15
>>> caller.send('goodbye')
result of 2nd yield: goodbye
return value of yield-from: done
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration
```

当`caller`从`gen`生成代理，`caller`并没有更进一步。注意到这些它的指令指针仍旧在15，也就是`yield from`声明处，甚至当内层生成器`gen`从`yield`声明到下一步。从我们的外层`caller`来看，我们也不能确定值是来自`caller`还是委托的生成器。对于内层的`gen`来说我们也不能确定sent是来自`caller`还是来之与外部。`yield from` 是一个无摩擦的通道，通过它的值的流入和流出`gen`直到`gen`完成。

```python
rv = yield from gen
```
早些时候，当我们批评基于回调的异步编程时，最为诟病的是关于"stack ripping"（堆栈翻录）：当我们的回调抛出异常的时候，栈追溯的类型无用。因为仅仅显示了是什么事件循环调用了回调，并没有说为什么，那么协程怎么样呢？

```python
>>> def gen_fn():
...     raise Exception('my error')
>>> caller = caller_fn()
>>> caller.send(None)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 3, in caller_fn
  File "<input>", line 2, in gen_fn
Exception: my error
```

这样的信息太有用了~！栈追溯显示了`caller_fn`为`gen_fn`的代理，当它抛出异常的时候。甚至，我们可以捕捉调用的子协程在异常句柄中，就像是调试子程序一样：

```python
>>> def gen_fn():
...     yield 1
...     raise Exception('uh oh')
...
>>> def caller_fn():
...     try:
...         yield from gen_fn()
...     except Exception as exc:
...         print('caught {}'.format(exc))
...
>>> caller = caller_fn()
>>> caller.send(None)
1
>>> caller.send('hello')
caught uh oh
```
于是 我们实际逻辑正如使用常规的子程序一样。让我们从`fetcher`得到一个有用的子协程。我们编写`read`协程来接收数据：

```python
def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))

    selector.register(sock.fileno(), EVENT_READ, on_readable)
    chunk = yield f  # Read one chunk.
    selector.unregister(sock.fileno())
    return chunk
```

我们将使用`read`来构建`read_all`的协程用于接收所有的信息。

```python
def read_all(sock):
response = []
# Read whole response.
chunk = yield from read(sock)
while chunk:
    response.append(chunk)
    chunk = yield from read(sock)

return b''.join(response)
```
如果你不看 `yield` 语句， 那么这看起来很像是阻塞i/o函数。事实上`read`和`read_all`就是协程，从`read`到暂停`read_all`，直到i/o完成。当`read_all`
暂停时，异步事件循环执行其他工作，并等待其他i/o事件，`read_all`在恢复事件准备好后，在下一个循环读取结果。

在根栈，`fetch` 调用 `read_all`：

```python
class Fetcher:
    def fetch(self):
         # ... connection logic from above, then:
        sock.send(request.encode('ascii'))
        self.response = yield from read_all(sock)
```

神奇的是，Task 这个类不需要做任何修改。它驱使外层的`fetch`协程和之前一样：

```python
Task(fetcher.fetch())
loop()
```

当`read`产生之后，task通过 `yield from`语句的通道来接受它，好像future直接从`fetch`产生。当循环解决future时，task将结果发送到`fetch`,并且读取接受该值，就像是task驱动的直接读取一样。

![img](http://aosabook.org/en/500L/crawler-images/yield-from.png)

为了完美的实现我们的协程，我们使用一个小技巧：我们的代码使用`yield`当它等待future，但是`yield from`当它代理子协程的时候。他更多的依赖使用`yield from`无论什么时候停止协程。然后协程并不需要关心他等待什么类型的事情。

我们使用py的高级特性迭代器和生成器。生成器对应调用者，对于调用者来说，迭代器也有相同的功效。所以我们通过一个特殊方法是我们的Future类可迭代：

```python
    # Method on Future class.
    def __iter__(self):
        # Tell Task to resume me here.
        yield self
        return self.result
```
future 的 `__iter__`方法是协程自己成成自己，现在我们替换这一段代码：

```python
# f is a Future.
yield f
```
和

```python
# f is a Future.
yield from f
```
输出是一致的！驱动任务接受自future的调用`send`,当future完成之后，它将新的结果发送回协程。

无处不在的使用`yield from`的优势是什么？为什么委托给子协程使用`yield from`比等待futrue使用`yield`效率更好？它的好处是在于，一个方法可以自由的改变其实现而不影响调用者：它可能是个正常的发发返回一个future将要解析的值，或者他也可能是个协同程序包含`yield from`语句，并返回值。在任何一种情况下，调用者只需要从方法中`yield`，以便等待结果。

各位，我们已经到达了异步协程的终点。我们探讨了生成器机制，并简单实现了一个future的任务。我们概述了异步如何实现最好的两个：并发i/o比线程更有效，比回调更清晰。当然，整整的异步比我们描述的要复杂的多。真正的框架解决了 0 拷贝i/o，公平调度，异常处理和大量的其他功能。

对于异步用户，用协程编码比你在这里看到的要简单的多。在上面的代码中，我们第一个实现的协程版本，所以你能看到回调，任务，和future。你甚至看到非阻塞socket和调用select。但是当时用异步构建项目的时候，这些将不会出现在你的代码中。正如我们承诺的那样，你现在可以顺利的获取url：

```python
    @asyncio.coroutine
    def fetch(self, url):
        response = yield from self.session.get(url)
        body = yield from response.read()
```
当我们介绍完这些基础的内容后，我们回到之前的任务：使用异步写一个异步网络爬虫。

## 协同程序
我们一开始描述了爬虫怎么工作。现在我们使用异步协程实现它。

我们的爬虫会从第一个页面开始，解析他的链接，然后添加到队列中。在这之后，他分离出网站，同事抓取页面。但是为了限制客户端载入的页面，我们希望运行的worker有个最大的数字，不用太多。不论何时workers完成页面抓取，他应该立即开始从队列中的下一个。当没有足够的worker的时候我们需要将一些worker暂停。但是当worker点击一个多链接的页面的时候，列队会突然增长，任何暂停worker都会恢复。最后，我们的层序必须在工作完成后退出。

假设我们的workers为线程。我们会怎么表达算法？我们可以使用标准库的同步队列。每一次想队列添加一个元素，队列就会增加其'task'的计数，worker的线程完成之后会调用`task_done`线程。主线程会在`Queue.join`阻塞，当队列中所有的`task_done`都匹配之后就会退出。

协程使用与异步队列相同的的模式！我们先import 它！

```python
try:
    from asyncio import JoinableQueue as Queue
except ImportError:
    # In Python 3.5, asyncio.JoinableQueue is
    # merged into Queue.
    from asyncio import Queue
```

我们在`crawler`类中收集worker的共享状态，并把`crawl`方法写入主逻辑。我们启动`crawl`协程并运行异步事件循环，直到`crawl`完成。

```python
loop = asyncio.get_event_loop()

crawler = crawling.Crawler('http://xkcd.com',
                           max_redirect=10)

loop.run_until_complete(crawler.crawl())
```
爬虫从根url和`max_redirect`开始,获取任意网页重定向的数量。将`(URL, max_redirect)`放入队列。（理由，关注）。

```python
class Crawler:
    def __init__(self, root_url, max_redirect):
        self.max_tasks = 10
        self.max_redirect = max_redirect
        self.q = Queue()
        self.seen_urls = set()

        # aiohttp's ClientSession does connection pooling and
        # HTTP keep-alives for us.
        self.session = aiohttp.ClientSession(loop=loop)

        # Put (URL, max_redirect) in the queue.
        self.q.put((root_url, self.max_redirect))
```

队列中未完成的任务数量为1.回到我们主函数，我们启动时间循环和`crawl`方法。

```python
loop.run_until_complete(crawler.crawl())
```

`crawl`协程启动workers。它就像一个主线程：阻塞在`join`直到所有的任务完成，而workers在后台运行。

```python
    @asyncio.coroutine
    def crawl(self):
        """Run the crawler until all work is done."""
        workers = [asyncio.Task(self.work())
                   for _ in range(self.max_tasks)]

        # When all work is done, exit.
        yield from self.q.join()
        for w in workers:
            w.cancel()
```

如果workers是线程的话我们不希望一次性启动他们。除非必要，应该尽量避免创建过多的线程，线程池通常根据需要增长。但是协程就很轻量，所以我们允许简单的一次性开始最大的数量。

有趣的是我们如何停止爬虫。当`join`future的时候，worker的task仍然存活但是被停职：他们等待更多的url，但是没有道理。因此主协程在推出之前取消了他们。否则，当py的解释器关闭并调用所有对象的析构函数的时候，这些tasks会强制结束：

```python
ERROR:asyncio:Task was destroyed but it is pending!
```

如何`cancel`work？生成器具有我们未展示的功能，能可以将异常从外部抛入生成器：

```python
>>> gen = gen_fn()
>>> gen.send(None)  # Start the generator as usual.
1
>>> gen.throw(Exception('error'))
Traceback (most recent call last):
  File "<input>", line 3, in <module>
  File "<input>", line 2, in gen_fn
Exception: error
```
生成器通过throw恢复，但他现在引发异常。如果生长期调用栈中没有捕获异常，则异常将会被顶部捕获，所以要取消任务的协程：

```python
    # Method of Task class.
    def cancel(self):
        self.coro.throw(CancelledError)
```

不论生成器在何处停止，在`yield from`语句，它恢复和抛出一个异常。我们在任务的`step`方法中处理取消：

```python
    # Method of Task class.
    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except CancelledError:
            self.cancelled = True
            return
        except StopIteration:
            return

        next_future.add_done_callback(self.step)
```
现在任务知道他被取消，所以当其被销毁的时候会正常退出。

一旦`crawl`方法取消了workers，它将会推出。事件循环意识到协程完成，也同样会退出：

```python
loop.run_until_complete(crawler.crawl())
```
`crawl`方法包含我们的主协程必须做的。他是worker的协程，从队列获取url，并解析他们的新链接，每一个worker的`work`的协程是独立的。

```python
    @asyncio.coroutine
    def work(self):
        while True:
            url, max_redirect = yield from self.q.get()

            # Download page and add new links to self.q.
            yield from self.fetch(url, max_redirect)
            self.q.task_done()
```

py解释器看到这段代码包含`yield from`语句，将他编译为生成函数。所以在`crawl`中，当住协程调用`self.work`十次，并不是真正的执行了这个方法：它仅仅创建了10个生成器对象。他在任务的包裹中。任务接收每个生成器的`yield`,并且通过调用`send`来驱动生成器与每一个future结果。因为生成器有自己的堆栈，所以他们独立运行，并且具有独立的局部变量和指令指针。

worker通过队列与协程协调。他等待以下内容：

```python
    url, max_redirect = yield from self.q.get()
```



