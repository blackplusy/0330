#coding=utf-8
#字符集(翻译官)
#utf-8  全能翻译官
#GBK2312 中文翻译官
#print() 函数是把括号中内容或者变量打印到屏幕上
#ctl+s 保存
#1.直接输出
print('simida')
print(100)

#2.变量输出
name='gaga'
print(name)
age=18
print(age)

a=100
b=30
print(a+b)
a='lady'
b='gaga'
print(a+b)

#3.函数输出
# len()   变量中元素的个数(长度)
# abs()   绝对值
name='wataxiwayaqiluobei'
print(len(name))
num=-30
print(abs(num))

#4.格式化输出
#  %s  格式化显示字符串
#  %d  格式化显示数字
# 格式化输出时候如果传入的是多个参数必须要加括号
'''
小明是第一
小红是第二
小军是第三
'''
name='heygor'
print('%s is so handsome!!!!!'% name)
age=18
print('%s的年龄是%d'%(name,age))
print('_______')
#print('%s的年龄是%d'%(age,name))












