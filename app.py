from flask import Flask, redirect, request, jsonify, Response, make_response, render_template

#实例化app，Flask是一个蓝图，你把它实例化成一个app对象
import settings

app = Flask(__name__)
app.config.from_object(settings)
data = {'a': '北京','b': '深圳','c': '广州'}
#用装饰器处理路由，route代表路由，加上@代表装饰器，app代表对象
#绑定一个路由
@app.route("/hello") #路由
def hello_world():   #视图函数   mtv: view 视图   函数
    return "hello world"


#再定义一个路由,传一个变量给路由，传一个自定义名字,默认为字符串类型
@app.route("/hey/<username>")
def hey_yingong(username):
    return "你的名字是: %s" % username

#定义一个路由，传一个字典里面的变量
@app.route("/getcity/<city>")
def get_city(city):
    return data.get(city)

@app.route("/my/<int:number>")
def my_number(number):
    return "my %d" % (number + number)

@app.route("/add/<float:money>")
def add(money):
    print('===',type(money))
    return str(money)

@app.route('/index/<path:p>')
def get_path(p):
    print('**************', type(p)) #str类型
    print(p)
    return p

@app.route('/test/<uuid:id>') #必须传递uuid的格式
def test(id):
    print('***********####',type(id))
    return '获取唯一标识码'

#重定向后访问这个网站后面加上后缀就能跳转到重定向的网站
#访问 http://127.0.0.1:5000/baidu---->会跳转到https://www.baidu.com页面
@app.route("/baidu")
def baidu():
    return redirect("https://www.baidu.com")


@app.route('/index')
def index():
    return {'a': '北京','b': '上海','c': '深圳',}   #json

@app.route('/index1')
def index1():
    return '<h1>北京<h1>'       #html；可以加h1标签(加粗)

@app.route('/index2')
def index2():
    return 'set',200       #使用元祖形式设置响应吗，返回一些用户可以观看的东西

@app.route('/index21')
def index21():
    s = '''
     <title>404 not Found</tittle>
     <h1>Not Found<h1>
    '''

    return s,404       #使用元祖形式设置响应吗，返回一些用户可以观看的东西

@app.route('/index3')
def index3():
    return Response('<h1>大家想好中午吃什么了吗？<h1>')   #可以加h1标签(加粗)

@app.route('/index4')
def index4():
    content = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
    <style>
        div{
            width: 100%;
            height: 100px;
            border: 2px solid burlywood;
        }
        </style>
</head>
<body>
<h1>欢迎来到小工具小组</h1>
<div>
    <ul>
        <li>hello</li>
        <li>abc</li>
        <li>world</li>
    </ul>
    
    <form action="" method="get">
        <p><input type="text" placeholder="请输入用户名"></p>
        <p><input type="text" placeholder="请输入地址"></p>
        <p><input type="submit" value="提交"></p>
    </form>
</div>
</body>
</html>
    '''
    response = make_response(content) #返回值就是一个response对象
    response.headers['mytest'] = '123abc'
    return response



#允许多种访问方式
@app.route("/test/my/first",methods=["POST","GET"])
def first_post():
    #这里表示你要输入的参数是json格式，以request方式进行发送
    my_json = request.get_json()
    print(my_json)
    #get_name，get_age表示你要输入那几个的参数
    get_name = my_json.get("name")
    get_age = my_json.get("age")
    #jsonify关键字表示我给你返回的数据是json格式的数据
    return jsonify(name=get_name,age=get_age)

#报错处理，正确提示
@app.route("/test/my/first/all",methods=["POST"])
def first_all():
    try:
        my_json = request.get_json()
        print(my_json)
        get_name = my_json.get("name")
        get_age = my_json.get("age")
        if not all([get_name,get_age]):
            return jsonify(msg="缺少参数")

        get_age += 10

        return jsonify(get_name=get_name, age = get_age)
    except Exception as e :
        print(e)
        return jsonify(msg="出错了哦，请检查是否正确访问")

@app.route("/index5")
def index5():
    print(request.headers)#request对象   可以访问属性和调用方法
    return 'welcom everyone!'

@app.route("/register1")
def register1():
    pass

@app.route("/register")
def register():
    r = render_template('rergister.html')    #render_template是flask自带的一个渲染函数，直接调用使用就行
    # print(r)
    return r

@app.route("/register2",methods=['GET','POST'])
def register2(): #获取页面提交的内容
    print(request.full_path) #/register2?username=seak&address=shanghai 全路径会拼接到游览器地址
    print(request.path)   #/register2
    print(request.args) #args将usernmae和address封装成一个字典，ImmutableMultiDict([('username', 'seak'), ('address', 'shanghai')])
                        #注意点：args只能取get请求的数据，post请求的需要其他方式
    print(request.args.get('username')) #根据key获取字典value的方式获取值seak
    print(request.args.get('address')) ##根据key获取字典value的方式获取值shanghai
    print(request.form)
    print(request.form.get('check')) #如果请求方式时post要使用form获取值

    return '进来了'

#使用session进行登录
@app.route("/try/login",methods=["POST"])
def login():
    pass

#检查session状态
@app.route("/try/session",methods=["GET"])
def check_session():
    pass

#使用session进行登出
@app.route("/try/login",methods=["GET"])
def login_out():
    pass




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
    #0.0.0.0表示任何主机都可以访问这个程序
    #port表示设置顶端口用命令行方式启动python 启动路径（eg:G:\Flask2\app.py），直接右键run会只调用pycharm本地的东西  适用于development(开发环境)
    #debug=True 开启（True）表示只要代码改变，服务器会试试重新加载
    #debug=False 默认关闭调式模式，代码发生改变不会自动加载，适用于production(生产)环境
