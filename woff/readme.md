# 前
这是16年最后一个项目，也是17年第一个玩具，得益于知乎的一篇文章，
爬虫与饭爬虫将会永远下去，
需要测试则运行

    wofffile.py 文件

如果需要解析公具 使用

    readwoff.py 文件
    {"uniXXXX":"[0-9]",.....,".":"."}
    如此结构

## 第一版
仅仅找出内容

## 第二版
将woff文件转换为otf
库为 woff2otf
通过 fonttools 转换成 xml
读取 xml 的id 偏移得到数据

## 第三版
读取woff 文件
获得id 与unicode的关系，得到映射关系