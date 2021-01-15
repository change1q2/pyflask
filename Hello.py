from flask import Flask, redirect, request,jsonify

#实例化app，Flask是一个蓝图，你把它实例化成一个app对象
app = Flask(__name__)


#用装饰器处理路由，route代表路由，加上@代表装饰器，app代表对象
#绑定一个路由
@app.route("/hello")
def hello_world():
    return "hello world"


#再定义一个路由,传一个变量给路由
@app.route("/hey/<username>")
def hey_yingong(username):
    return "hey %s" % username

@app.route("/my/<int:number>")
def my_number(number):
    return "my %d" % (number + number)

#重定向后访问这个网站后面加上后缀就能跳转到重定向的网站
#访问 http://127.0.0.1:5000/baidu---->会跳转到https://www.baidu.com页面
@app.route("/baidu")
def baidu():
    return redirect("https://www.baidu.com")

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



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
    #0.0.0.0表示任何主机都可以访问这个程序