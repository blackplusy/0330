#coding=utf-8
#1.实参位置
def info(name,age):
    print('名字是%s,年龄是%d'%(name,age))
info('heygor',18)
#info(18,'08ma')
#2.关键字参数
def animal(pet1,pet2):
    print(pet1+'汪！ '+pet2+'喵！')
animal(pet2='jiafei',pet1='2ha')
#3.参数默认值
def userinfo(name,minzu='汉'):
    print('您的名字是%s,你的民族是%s'% (name,minzu))
userinfo('heygor','穷')
userinfo('simida')
#4.不定长参数
def tag(x,y,*args):
    print(x,y,args)
tag('帅气','威猛','呵呵','吹牛逼','喊麦！')

def tag1(x,**args):
    print(x,args)
tag1('帅气',肤色='黑',脾气='爆')