from flask import Flask

app = Flask(__name__)
print(app.config)
#修改配置文件内容，这里加配置会越加越多，所以一般做解耦处理另外新建一个setting文件用app3.py加载
app.config['ENV'] = 'production'
app.config['DEBUG'] = True



@app.route('/')
def index():
    return '欢迎大家！····'


if __name__ == '__main__':
    app.run(port=8000)

    # # print(app.config)
    # # 将setting文件中的配置项拉取过来使用
    # app.config.from_object(settings)