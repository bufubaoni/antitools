# 说明

## celery
windows 平台只支持 到 3.1

使用4.1 会报错误

启动如果要拿到结果，需要设置`backend` 启动的时候 需要
设置`broker`否则就是不能导入 文件名
## rabbitmq
使用配置文件设置的时候，设置中项会添加一个 逗号  导致配置有问题
