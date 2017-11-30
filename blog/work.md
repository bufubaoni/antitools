# 工作相关
## 登陆验证
token 验证 作为装饰器统一验证，验证通过后返回主逻辑
## 接受参数，返回结果，异常处理
由于数据比较统一，统一处理参数，和返回结果，有意想不到的惊喜

## swagger
丝袜哥，对url，请求参数，返回结果都有好的生成记录，希望自己对`restful`此装饰器进行统一的添加。

## 假设
任何公司都需要盈利。
应用架构
对单表数据进行抽象提供对系统级别的接口
delete 各个版本不同
好像又一种有意思的东西，哈哈，简直有意思
django 内部的路由，
前后分离的问题
将django 做成flask风格的代码，并不是什么好的创意，可能实现的方法还有问题，因为用了最简单的 方法
有时候业务和技术是密不可分的，单单脱离了什么都会缺少什么。

## 源码阅读
老师教你的也就是入门，然后剩下的就是领悟了，绘画无非是各大美术馆，而各大开源项目就像是巨大的美术馆。
对oauth 的阅读。待讨论中四种模式，标准模式，简k模式，密码模式，客户端模式
其中客户端模式更像是api调用。密码模式更像是代理。
使用soap但是又不完全使用。
不过将 django 中集成如 pysimplesoap 也还不错。再做一下 dispatch 基本上就满足要求了。
想将pysimplesoap 这个框架集成方式开源出来。
而且将刨析oauth这个方式写一下。 
很多收旧应该使用订阅模式解耦然而并没有
过分的依赖cbv会有意想不到的 bug，当然写起来很爽，其实也不算是bug吧，只不过需要每次需要初始化一下公共变量
在看pysimplesoap 的源码

## websockets
使用uwsgi+django 启动的websocket长链接就会阻塞线程，如果不使用异步就会导致进程阻塞
最终使用了 eventlet 启动wsgi 应用，在此作笔记
使用 uwsgi 启动eventlet进程后，并发一直撑到750 进程挂掉了，然后nginx 不再转发websocket 内容，即websocket不再请求页面，导致效率极低
真的 eventlet 后撑到1300 的客户端，还没找到什么好方法, 同步进程 却是只能抗到几个并发，如果要应用于生产，依旧需要异步进程。

也不知道写点什么，就当牢骚一点吧，最近工作还可以。
搭建了 jupyter 环境，但是还没想好怎么用。

用于user登陆登出的问题
由于现在已经耦合了11个项目了。简直不敢大改了
只好做出 前端模拟登出，然后删掉headers的方案来模拟登出

除了更改表结构，目前还没想到有什么 能灵活满足需求的登陆方式，而且很多老项目柔和在一起，想想就很恐怖了。

同样又考虑了 项目之间的柔和，之前的问题，貌似可以 提供不同的登陆方式，例如token和session 的登陆，不过对之前项目影响很大，还是采取比较小的方式。
现在写代码之前，要考虑之前项目的影响，和新项目的规模，希望都在掌握之中吧。
我想websocket 出了一点问题，看来线程对于python还是不要说了吧
还有个kafka的问题，之前一直在用线程来跑的循环，现在想想也是隐患吧

websocket 到现在应该算是一段落了，如果还有问题的话，只好推迟了

接手前使用，单进程，单线程跑
导致在维持长连接的时候阻塞进程，导致其他页面不能访问

使用多线程
在更换协程（eventlet）启动后不存在进程阻塞了
线程主要用于发布kafka 的消费者

问题就是 线程之间的共用内存，和gil 的问题，导致有时会锁死在单个线程，其他线程不存在切换，导致有些消息不能及时发布

使用多进程
在寻求帮助之后，发现问题在于kafka的进程阻塞，两种解决办法，第一种使用kafka的异步队列，订阅其消息，然后进行回调
第二种，就是将发布写成服务，一旦有订阅，会请求此服务，避免了同一个项目多个线程的问题。
现阶段启用第二种方式，希望稳定性会很好

## kafka
之前一直没怎么用过消息队列，用起来其实很方便，应该是因为项目比较小，所以很难遇到性能的瓶颈吧

奇怪的问题，group id 有一个组居然总是会拿到历史数据，过了一天之后，有莫名其妙的好了。
同样的问题有复现，却不知道怎么复现的 这样的问题就同样出现了。

在特殊情况下 get_manager_id 会返回一个 none 然后会导致程序崩溃

## nginx
有一个接口响应慢，拖慢了整个进程，然后导致一直报 broken pipe error 32 这样的 错误。

## mysql
很多情况下 因为sql导致语句执行慢，拖慢整个接口速度，大部分问题可以通过索引的修改

## django

针对多表回滚，django也有，

```python
from django.db import transaction
```
django 使用session进行认证，如果同时接口使用drf之后，使用login_required 方法，就会报错，仅仅使用request.user.id 可以判断是否有用户登陆。
在对django rest framework 框架进行使用中发现，其default auth 并不是很个性化，其中如 头字段缺失，没有在数据库中，这些问题，都不会经过用户代码，而是直接粗粝，缩影并不是很友好
当然包括了请求数据的验证，
## 代码风格
 现在，代码的风格是一个很玄妙的东西，在函数入口我认为 将局部变量声明比较好，虽然python是一种很灵活的语言，可以容许你可以在使用的时候任意声明，但是也造成了一定的困扰。
最终使用了django的form 做了封装，当做入参的检查的工具,
重写的 restframe 的dispatch 顺便看了他的 源码，感觉他的并不是很优美，很多东西 并不是 一次加载的。很多 都找来找去。

在使用django  cbv 的时候，如果单单将一个方法赋予变量，python 会默认将self 作为参数传入函数
目前是用 反射解决，期待更好的解决

```python
from rest_framework.views import APIView
import steps
class DemoView(ApiView):
    LOGIC_METHOD = None

    def get(self, request):
        method = getattr(steps, self.LOGIC_METHOD)
        return method()


class CompanyAlarmView(DemoView):
    LOGIC_METHOD = "some_method"
```

原本希望通过 如下调用,但是使用这种方法会想 some_method 中传入self 参数
```python
from rest_framework.views import APIView
from steps import steps
class DemoView(ApiView):
    LOGIC_METHOD = None

    def get(self, request):
        method = self.LOGIC_METHOD
        return method()


class CompanyAlarmView(DemoView):
    LOGIC_METHOD = some_method
```

`steps.py` 文件内容

```python
def some_method(agr=default):
    return agr
```


## gevent

询问朋友之后，说是不能 一直loop 只能保证 其不阻塞，不过可以将一个 循环放入其中作为beat来调用 一个任务列表来作为调用，这样就简单的做了一个timer 的定时器，当然时间不是很准，

如果再做一个 监听 端口的话，就可以简单的做一个非阻塞的任务列表，当然这个是非常简陋的列表

## 周报
我 觉得我还是需要一个 周报自动生成的 东西，虽然有了 trello 和 tower ，但是 生成的 太烂了,改为了 tower 发布周报，至于有什么用，各有各的看法了。

## api service
在上一个新技术的前提就是对他做好调研，重要的是要解决什么问题，一定要找到问题所在，并非听说了一门新技术就要上。就这么简单
还没有拆分，只是进行了 简单的归类，就已经划分出9个项目，如果需要拆分部署，不知道工作量是多大。

## 闲谈
或许今天做的事情看起来完全没有意义，只有回看的时候才能发现其特别的价值吧。

## git
记得刚学习python 的时候，有一本书上讲了python 和 svn，那时候哪里懂得svn是什么东西，就是觉得是很神秘，并且深奥的根本听不懂的，当然，事实证明却是没听懂，那本书，也在看了20多页之后就放弃了。
初学者或许真的不需要一下输入那么多东西，只有在懂了一个之后，再去学习另一个，接受起来会比较简单。当然如果已经掌握一门语言后和初学者就完全不同了。

分了几个分支，之前就的流程 重新合并，会有一点问题，不过加油

## 杂谈
学习是一个自然而然的过程，如果一个人现有的知识到达了一定程度就会自发的进行学习，反之亦然，如果有人单纯的追求形式上的成熟必然不会有什么理想的结果。

## redis
### 集合操作
- SADD---------向集合中添加元素，`sadd key value`
- SCARD--------集合元素个数，`scard key`
- SDIFF--------第一个集合与之后集合并集的差集，
- SDIFFSTORE
- SINTER
- SINTERSTORE
- SISMEMBER----元素是否在集合中,`sismember key value`
- SMEMBERS
- SMOVE--------移动出指定元素 `smove key dst value` 将 key中的 value 移动到 dst 中
- SPOP
- SRANDMEMBER
- SREM---------移除指定元素 `srem key value`
- SSCAN
- SUNION
- SUNIONSTORE

### hash操作
- HSET----------向hash中添加元素
- HGET----------从hash中取出元素
- HEXISTS-------has中是否存在元素


使用cache将一定model中的一定数据缓存到redis中，可以通过简单的装饰器进行数据的缓存，主要针对的是model 的方法

在对diango 的manager 进行一系列的魔改之后，为了实现view 业务中代码不改变而直接获得缓存数据
```python
class CacheManager(models.Manager):
    def get_queryset(self):
        query_set = super(FBDicManager, self).get_queryset()
        self.query = query_set.query
        self.model = query_set.model
        self.filter = query_set.filter
        query_set.get = self.get
        return query_set

    def get(self, *args, **kwargs):
        convert = {"pk": "id",
                   "id": "id"}
        j_query = {int(item.get("id")): item for item in self.model.query_all()}
        j_model = j_query.get(int(kwargs.values()[0]))
        if j_model:
            return self.model(**j_model)
        else:
            return None
```
主要针对的是单一查询，也就是使用pk或者 id 查询，当然 convert 并没有用，此时如果返回dic表中数据，则会从缓存中直接拿取。


## pydal
可以使用_select 用于生成sql 而不进行数据库查询，对此可以进行其他数据库连接，或者 放入队列中，依次入库

是不是可以 仅将插入，删除 作为冷数据 保存在内存中，等数据冷之后 落地到数据库，然后将更新操作放到内存中，等需要落地的时候在依次入库，当然由于数据只有一个，可以将redis 的自增作为全局的id

## logging
python提供了方便的 logging模块，尤其是  root logger 使得整个项目使用起来非常方便。程序需要一个 main 入口，然后会依次 调用这个logging

## pymysql

之前有个同事问我  为什么格式化的时候总是出错误，今天终于有时间来 处理这个问题，就看了看，发现 使用 pymysql.excute 的时候 向其中传参数 也就是 args 的时候 总是提示语法错误
    cur.mogrify("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))
    "INSERT INTO test (num, data) VALUES (42, E'bar')"
会被解释成下边一种，这是正常使用，但是当使用格式化表名的时候
    cur.mogrify("INSERT INTO %s (num, data) VALUES (%s, %s)", ('test', 42, 'bar'))
    "INSERT INTO 'test' (num, data) VALUES ('test',42, E'bar')"
为了防止注入 会将表名 解释成 带有双引号的 ，这个是 sql 的本身占位符的问题，
解决此问题的 途径就是
    cur.mogrify("INSERT INTO {tablename} (num, data) VALUES (%s, %s)".format(tablename='test'), (42, 'bar'))
即可解决问题。

### flask 相关

初步使用flask 和 pydal 对之前的数据库做了一下测试，感觉还可以，想对 flask 进行初步的改造一下，首先就希望可以支持 url 这样的项目管理，毕竟装饰器做的路由，虽然好看 ，但是维护起来，还是有一点困难的

使用了 legacy table 这样的工具，当然自己也为其写了一个 filter，现在 对于 数据库操作，更接近于 原生的 sql 而不是如 django一样 orm 的操作。

### 项目拆分

之前没觉得怎么样，总是写到一个项目，今天梳理起来，大大小小16个项目，仅仅是梳理了一下，不过有些没有用了，有些也比较麻烦。

### 基础数据服务

由于很多接口类似，所以计划将基础接口梳理出来，并进行拆分合并。
对数据表进行了瘦身，将数据量大的表改变了其访问方式，只对其进行增加，而不做修改。修改状态则放到另外的数据表中，当前状态放到对应表中，此次对数据库表结构做出了较大的调整。

### csrf 问题
csrf 是个奇怪的问题，当cookie中含有sessionid（网站认证id）的时候会触发csrf检查。

一个机缘巧合的机会询问到，这个确实是一个坑，需要在 view 的最外层加上csrf_exempt 这个装饰器，由于我继承的是 drf的APIView在最层的 as_view()已经做了csrf_exempt 处理，当时他告诉我由于这个位置不够外层，所以需要再最外层加上这个方法，发现这个问题并不能解决，最终解决还是将`SessionAuthentication`里边的那个`enforce_csrf`pass掉了，
当然最好的解决方法仍然是 写一个类的装饰器，直接重写掉这个方法，以后可以 方便的导入,相同的问题应该只解决一遍。类的装饰器实现起来还是很方便的，这里就不多做叙述了，和csrf 的斗争也算告一个段落了。

### nginx

一直认为nginx 不能用url 作为分割，后来仔细阅读文档发现，nginx 支持以uri开头作为路由，而且可以对项目拆分有很乐观的，并且根据不同的static可以路由到不同的项目文件夹，也为项目上传提供了方便。

并且如此 作为反向代理，也不会出现跨域问题。

今天做了部分拆分，发现单进程程序会出现，阻塞的问题，不知拆分后如何

忙碌的一天

针对多次查询的优化，

发现有一个循环查询了很多次，于是临时做了一个局部缓存，对数据只查询一次，继而缓存到变量中，当此变量超出作用域后即刻销毁。

django 的生成limt 的效率非常低，如果数据量不大建议全部查询出来，然后再做分割，而不是直接使用切片生成limt 语句（主要会乱使用索引）

仍然优化中，遇到django分页问题，会先 count 再做分页，如果数据量非常大的话会导致此语句非常慢，目前没找到优化方法

如果是新系统的话，建议一开始做好异步准备，做好数据分析，提高可复用性。

### django session

遇到平移修改接口的时候，会遇到直接想写一个 class 直接 引用 view 的情况，如果遇到此种情况，可以直接 request.set_test_cookie()

然后将直接调用此类 即可
```python
    ma = SomeViews().as_view()

    request.session.set_test_cookie()
    # 正常使用即可，如果需要区别，那么 系统会自动分辨
    return ma(request)
```
如果使用 token 登陆就比较方便了，直接 传入，然后再次基础上 做验证就可以了。


### django数据库

django对于每一请求会新建一个数据库连接，当连接 超过限度的时候，数据库会拒绝连接，连接关闭 自view 结束，当有些view 时间很长的时候，会导致一直不出view，在接口时间长的接口需要手动关闭数据库连接

django本身使用orm 是懒加载，昨天就犯了一个错误，在使用orm查询的时候 先使用了  if query_set   这样的查询，导致进行了查询，所以改写了query_set 进行条件是否存在的查询判断，然后再进行分页，而后进行关联查询，速度才算正常
### celery

调试的时候，需要

from from celery.contrib import rdb

rdb.set_trance()

然后 需要启用 telnet 客户端，连接到调试上。如果是win 的话需要启用此客户端

celery 有时无法使用 root 权限启动，需要手动 允许

from celery import platforms

platforms.C_FORCE_ROOT = True


工作之余希望能找一个lua 的ide，希望有些事情能交给proxy层做，因为毕竟server层的运算或者代价还是挺大的。

服务器认证，是无论如何的架构都绕不开的话题，现在有很多的方式进行认证，从远古的无法差别的请求，到cookie认证，再到session 认证，后来前后分离之后的 auth认证，认证过程无非是 密码，短信，u盾，指纹，

我记得当年有个将军令，可以保证服务器端和客户端有相同的验证码，也无非是算法 不同的hash

系统陆续做了 几次升级，效果还是不错，有时候 硬件会私自改动协议格式，给人造成了不小的困扰，不过好像也没什么好的办法，除非修改代码，或者做热补丁，

如果使用热补丁，那么一定要约定好协议，不要只做一次的事情，不过对于动态性语言，热补丁也不是很奇怪的事情，如果是静态编译型的，那么 肯定就需要约定好接口，进行开发

又发现了一个尴尬的问题，当models 和 数据库中的 columns 不是对应的时候 会报 operaerror 不过 代码 也可以 用错误编号 来判断，然后做正则，可以 提取表名，对于一些错误可以准确定位，

其实更深层的原因是，为什么总是改变 数据库的 数据结构呢。

今天 大神 突然问想做一个 logging 的分布式，原因很简单，多个进程共享logging 的时候 并不是进程安全的，所以 需要统一入库或者统一放到文件中，而切割的时候可能会进程之间发生冲突，导致数据无法添加，

其实logging 模块提供 sockethandler 可以方便的设置 请求地址和端口，当然 后续 tcp 连接可以使用 twist 进行入库，反正对于，效率也还可以，在 learnpython/sock.py 这个文件就是 日志服务器的 雏形

# signals

原本系统中集成了 一部分的 blinker 来进行 pub 和 sub ，后来在做 数据发送和交互的时候发现 django已经 继承了signal，当然细究的话 signal 也是同样用了 blinker 这个比较小众框架，其实是有这样一个需求，

数据入库的时候会请求一个 url地址，然后将处理过的 数据以data 的形式发送过来，这样接口设计的时候，每次都会重复的设计这个逻辑，而且毕竟http协议不如 程序内部处理

然后使用习惯也是这个样子，在 pub 的view 或者文件需要 import sub 这个模块这样才能正常的时候，如果订阅了这个sub 的话，那么 此时系统仅仅需要一个 接口来 接受即可，其他模块仅仅需要订阅 即可，相对也提高了系统的效率

当然先天性的 这个模块是个同步的 ，仅仅是定义了 callback 如果想要真正的提高效率，还是需要异步操作，剩下 怎么处理 异步的操作，就需要另作处理了。

## 再谈编码
由于写py比较多所以遇到编码错误本来就是一个常见的错误，本身就是千奇百怪的，甚至不同的人会遇到不同的错误，本质上 还是没有弄清楚什么是encode 什么是 decode ，前不就遇到了一个 unicode 的错误，

str(a) 程序员使用这样的一个简单的str 将整型转换成str 这么一个简单的代码，在线上也没有遇到任何问题，由于最近在对线上项目进行拆分，就会报出unicode的错误，问题解决起来很简单，仅仅需要将unicode捕获以后直接赋值给这个变量就可以了进行正常的拼接了。

当然有一个小问题就是，为什么线上没有，而拆分之后就有这个问题，这个问题同事在拆分的另一个子项目又出现了，直接去了拆分的子项目带环境的全面验证一下，发现有一个项目就不会出现这个问题，在view 的最顶端发现了一行`sys.setdefaultencoding('utf-8')`所有的问题就明了了，由于这个并没有在所有项目引用，所以导致部分有问题，部分没问题。当然在这里也做一下记录，这个可以改变当前运行的默认编码，所以str(unicode)的时候就会自动转化为有编码格式的字符串。

## form 验证
在接口的编写过程中我发现了一个非常蹩脚的问题，就是form表单的认证，由于本公司 是文档驱动开发，会做出一些奇怪的限制，例如id 数据库中为int 类型，文档就会写为string 类型，此时如果传过来一个 字符串就会存不进去，当然可以再view 中重新做判断，或者form 做一次数据转换为默认值，如果这个字段可传可不传的时候，文档会写出一个 字段必传，但是可以如果没有的时候为空 字符串
这样一个尴尬的过程，其中判断当然是比较蹩脚。