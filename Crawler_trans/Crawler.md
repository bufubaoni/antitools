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
