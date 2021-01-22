from flask import Flask

import settings

app = Flask(__name__)
# print(app.config)

# 将setting文件中的配置项拉取过来使用
app.config.from_object(settings)



@app.route('/')
def index():
    return '欢迎大家！····'


if __name__ == '__main__':
    app.run(port=8080)