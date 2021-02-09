from flask import Flask,request,render_template
import settings
app = Flask(__name__)

app.config.from_object(settings)

@app.route('/show1')
def show1():
    girls = ['如花','凤姐','宋宋','孙艺珍','林絮儿']
    users = [
        {'username': 'zhangsan0', 'password': '123', 'addr': 'beijing','phone':'1389375671'},
        {'username': 'zhangsan1', 'password': '123', 'addr': 'shanghai', 'phone': '1389375611'},
        {'username': 'zhangsan2', 'password': '123', 'addr': '重庆', 'phone': '1389375672'},
        {'username': 'zhangsan3', 'password': '123', 'addr': '深圳', 'phone': '1389375673'},
        {'username': 'zhangsan4', 'password': '123', 'addr': 'beijing4', 'phone': '1389375674'}
    ]
    return render_template('show_1.html',girls=girls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.run()