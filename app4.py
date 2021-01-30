from flask import Flask,request,render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)

class Girl:
    def __init__(self, name, addr):
        self.name = name
        self.gender = '女'
        self.addr = addr

    def __str__(self):
        return self.name
@app.route('/show')
def show():
    name = '沈凯'
    age = 18
    friends = ['建议', '陈静', '悦悦']
    dict1 = {'gift': '大手镯', 'gift2': '鲜花'}
    #创建对象
    girlfriend = Girl('美美', '安徽')
    return render_template('show.html',name=name, age=age,gender='男',friends=friends,dict=dict1,girlfriend=girlfriend)

if __name__ == '__main__':
    app.run()