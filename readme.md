# shadowsocks-py
python写的ss5连接翻墙工具。[这里](https://github.com/gavin-account/shadowsocks-over-websocket)有个node版的实现，本次使用python实现。

[这里](https://github.com/gwuhaolin/blog/issues/12)还有一份go语言的代码实现。

# 环境
## 库管理工具
本系统使用pipenv为第三方依赖包的管理。使用下面的命令安装pipenv：

```
>pip install pipenv
```

关于pipenv的使用可以参考：https://blog.windrunner.me/python/pip.html

## 云平台
本系统基于Python进行搭建，相关的python example可以参考heroku给的官方项目：
https://github.com/heroku/python-sample

### Procfile文件
这个需要查看heroku官方的[文档](https://devcenter.heroku.com/articles/procfile)。

### requirements.txt
使用pip安装的软库列表，官方是要安装flask，我们这里可以不安装，但是可以做一个查看界面，所以可以添加。

### app.py
这个是flask的使用文件，我们可以使用自己，也可以使用自己的server.py。本次打算直接在app.py中去启动flask，建立一个worker来处理server.py

## 代码分析
本次我们使用的代码规范分析是[Pylint](https://www.pylint.org/)。你需要使用下面的命令进行安装：
```
> sudo python -m pip install -U pylint
```

如果你不想看官方英文文档，可以阅读[这篇](https://www.ibm.com/developerworks/cn/linux/l-cn-pylint/)中文博客。

## 配置文件的读取
使用ini文件进行项目配置文件的处理。

## 日志

