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

下面通过一个*Processor*的例子
