Blinker
===================================
Blinker 提供快捷的基于对象的广播订阅

Blinker 内核小但是功能强大

    * 全局命名订阅
    * 匿名订阅
    * 自定义名称注册
    * 永久或临时订阅
    * 通过弱引用自动关闭连接
    * 发送任意数据
    * 收集订阅者的返回值

Blinker 作者为Jason Kirtand 遵循MIT协议，使用高于Python 2.4，3.0， 或者Jython2.5以上，PyPy 1.6 以上

## 订阅去耦
*signal()*方法创建一个新订阅

    >>> from blinker import signal
    >>> initialized = signal('initialized')
    >>> initialized is signal('initialized')
    True

当调用*signal('name')*返回一个订阅的单例，允许未连接部分(模块,插件,任何地方)调用而不需要导入其他代码。

## 订阅者
*Signal.connect()*注册一个可调用的函数每次广播消息时被调用。订阅者的函数也会在消息发布时被调用。

    >>> def subscriber(sender):
    ...     print("Got a signal sent by %r" % sender)
    ...
    >>> ready = signal('ready')
    >>> ready.connect(subscriber)
    <function subscriber at 0x...>

## 消息广播
消息会通过*Signal.send()*方法广播到订阅者。

下面通过一个*Processor*的例子，当例子运行时会发布*ready*的消息，当完成的时候会发送*complete*的消息。它将*self*传递给*send()*方法，表示此实例是消息的发布者。

    >>> class Processor:
    ...    def __init__(self, name):
    ...        self.name = name
    ...
    ...    def go(self):
    ...        ready = signal('ready')
    ...        ready.send(self)
    ...        print("Processing.")
    ...        complete = signal('complete')
    ...        complete.send(self)
    ...
    ...    def __repr__(self):
    ...        return '<Processor %s>' % self.name
    ...
    >>> processor_a = Processor('a')
    >>> processor_a.go()
    Got a signal sent by <Processor a>
    Processing.

*complete*消息在*go()*函数中，但是没有订阅者订阅*complete*消息，但是合法的。调用*send()*发送消息的时候如果没有订阅者，消息将不会发送（不必要的消息不发送，这是系统优化而来的）。

## 订阅特殊消息
消息发布时默认订阅者都会被调用，*Signal.connect()*方法接受可选参数来更严格的订阅一个消息发布：

    >>> def b_subscriber(sender):
    ...     print("Caught signal from processor_b.")
    ...     assert sender.name == 'b'
    ...
    >>> processor_b = Processor('b')
    >>> ready.connect(b_subscriber, sender=processor_b)
    <function b_subscriber at 0x...>

此方法只广播到实例*processor_b*，其余实例只能广播*ready*方法。
    >>> processor_a.go()
    Got a signal sent by <Processor a>
    Processing.
    >>> processor_b.go()
    Got a signal sent by <Processor b>
    Caught signal from processor_b.
    Processing.