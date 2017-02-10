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
