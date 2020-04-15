#coding=utf-8
#1.一个返回值
def sum(a,b):
    jisuan=a+b
    return jisuan
a=sum(10,20)
print(a)
#2.多个返回值
def ret(a,b):
    a*=10
    b*=1000
    return a,b
num=ret(10,8)
print(num)
print(type(num))

num1,num2=ret(3,5)
print(num1)
print(num2)