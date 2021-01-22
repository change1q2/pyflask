import uuid

#获取一个uuid的唯一标识
uid = uuid.uuid4()
print(uid)
print(type(uid))
#将uuid转义成字符串再去除-使用replace关键字
uid1 = str(uid).replace("-","")
print(uid1)