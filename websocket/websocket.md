# websocket 笔记
客户端由
- websocket.js
- swfobject.js
两者提供，
- ws://127.0.0.1:8888/realtime/mygroup

- 其中*realtime* 和 **mygroup** 为订阅，相同的才可以建立连接，

而后端相同的订阅频道可以进行消息推送

实在没什么好写的了，已经封装成这样了。