#coding=utf-8
#1.单继承
# class dog:
#     def __init__(self,name,color='black'):
#         self.name=name
#         self.color=color
#     def run(self):
#         print('狗富贵,互相旺！！！')
#
# class taidi(dog):
#     def setname(self,name):
#         self.name=name
#     def eat(self):
#         print('im eating!')
# gou=taidi('taitan')
# print('狗狗的名字%s'%gou.name)
# gou.eat()
# gou.setname('simida')
# print('狗狗的新名字%s'%gou.name)
# gou.run()
#2.多继承
class a:
    def printa(self):
        print('---a----')
class b:
    def printb(self):
        print('---b---')
class c(a,b):
    def printc(self):
        print('---c---')
c1=c()
c1.printa()
c1.printb()
c1.printc()