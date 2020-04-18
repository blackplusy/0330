#coding=utf-8

class student:
    def study(self):
        print('im study')
    def play(self):
        print('playing ball')
heygor=student()
#产生一个student对象，通过heygor实例来访问属性和方法
heygor.age=18
#给对象添加属性
heygor.face='black'
heygor.favor='basketball'

#实例访问类的方法
heygor.study()
#实例访问属性
print(heygor.favor)
#创建一个对象理解为通过模型创造实物





