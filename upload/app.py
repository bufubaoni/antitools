#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/30
from bottle import route, post, request
import bottle

app = bottle.default_app()


@route("/upload")
@post("/upload")
def upload():
    if request.method.lower() == "post":
        file = request.files.get("file")
        file.save("img/" + file.filename)
        return file.filename
    else:
        return ("<form method='post' action='/upload' enctype='multipart/form-data'>"
                "<input type='file' name='file'/>"
                "</br>"
                "<input type='submit'/>"
                "</form> ")


if __name__ == '__main__':
    bottle.run(app=app, host="0.0.0.0", port=8000, reloader=True)
