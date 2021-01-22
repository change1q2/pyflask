from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello World'

#WSGI:Web服务器网关接口（Python Web Server Gateway Interface，
# 缩写为WSGI）是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。
if __name__ == '__main__':
    app.run(port=8000)