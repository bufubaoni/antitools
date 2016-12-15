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
## 参数和返回值
*send()*可传递关键字参数，这些参数将会被转发给订阅者的方法。

    >>> send_data = signal('send-data')
    >>> @send_data.connect
    ... def receive_data(sender, **kw):
    ...     print("Caught signal from %r, data %r" % (sender, kw))
    ...     return 'received!'
    ...
    >>> result = send_data.send('anonymous', abc=123)
    Caught signal from 'anonymous', data {'abc': 123}
*send()*的返回值将会整合到一个集合中，此集合的元素为(订阅者方法，返回值):
    >>> result
    [(<function receive_data at 0x...>, 'received!')]
## 匿名消息
消息并不强制命名，*Signal* 构造器会在调用时创建唯一消息。例如，将上面的 *Processor* 两个消息改成属性即可。

    >>> from blinker import Signal
    >>> class AltProcessor:
    ...    on_ready = Signal()
    ...    on_complete = Signal()
    ...
    ...    def __init__(self, name):
    ...        self.name = name
    ...
    ...    def go(self):
    ...        self.on_ready.send(self)
    ...        print("Alternate processing.")
    ...        self.on_complete.send(self)
    ...
    ...    def __repr__(self):
    ...        return '<AltProcessor %s>' % self.name
    ...
## 装饰器
其实*connect()*方法返回一个订阅者，所以*connect*可以当作一个装饰器：

    >>> apc = AltProcessor('c')
    >>> @apc.on_complete.connect
    ... def completed(sender):
    ...     print "AltProcessor %s completed!" % sender.name
    ...
    >>> apc.go()
    Alternate processing.
    AltProcessor c completed!
方便之余，*sender*和*weak* 并不支持装饰器，但是可以使用*coneect_via()*方法代替：

    >>> dice_roll = signal('dice_roll')
    >>> @dice_roll.connect_via(1)
    ... @dice_roll.connect_via(3)
    ... @dice_roll.connect_via(5)
    ... def odd_subscriber(sender):
    ...     print("Observed dice roll %r." % sender)
    ...
    >>> result = dice_roll.send(3)
    Observed dice roll 3.
## 订阅优化
消息被非常快的发送，无论订阅者是否订阅，*receivers*属性可以有效的检测关键字的传递。

    >>> bool(signal('ready').receivers)
    True
    >>> bool(signal('complete').receivers)
    False
    >>> bool(AltProcessor.on_complete.receivers)
    True
## 订阅文档
命名和匿名的消息都可通过 *doc* 参数在构造时传递 pydoc 消息的帮助文档 。此文档可被大多数的文档生成器识别（如sphinx），并且非常适合同消息的其他数据一起发送。
