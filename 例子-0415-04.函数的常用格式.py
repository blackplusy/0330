#coding=utf-8
#1.无参数，无返回值
def jia():
    num1=input('num1>')
    num2=input('num2>')
    print(num1+num2)
jia()
#2.无参数，有返回值
def login():
    username=input('insert your name:')
    return username
name=login()
print('your name is %s'% name)
#3.有参数，无返回值
def login1(name,passwd):
    if len(name)>=5:
        print('输入合理')
        if passwd=='12345':
            print('登陆成功')
        else:
            print('密码有误')
    else:
        print('字符过短')
login1('simida','12345')
login1('aaa','123')
#4.有参数有返回值
def click(name):
    if len(name)==0:
        return 'success'
    else:
        return name
c=click('')
print(c)