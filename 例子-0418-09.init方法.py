#coding=utf-8
class student:
    def __init__(self):
        self.boy=20
        self.girl=30
    def study(self):
        print('good good study')

simida=student()
#实例化student类对象为simida
print(simida.girl)
print(simida.boy)
#没有创建对象时候是没有调用init方法就有两个属性，init方法创建对象后被默认调用
#__init__(self,name,age)第一个参数self代表自己，创建对象时候只需要self后面传入其他参数即可