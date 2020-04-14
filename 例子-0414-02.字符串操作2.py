#coding=utf-8
#find和index
a='c'
str1='aabbcc'
print(str1.find(a))
a='d'
print(str1.find(a))

a='b'
print(str1.index(a))
a='d'
#print(str1.index(a))
#isalpha()和isdigit()
a='simida'
print(a.isalpha())
a='321simida'
print(a.isalpha())
a='123'
print(a.isdigit())
a='123a'
print(a.isdigit())
#upper()和lower()
name='Apple'
print(name[2].upper())
print(name.lower())
#startswith和endswith
a='aabbcc'
print(a.startswith('a'))
print(a.endswith('d'))
#count、replace、split
name='heygorGaGa'
print(name.count('a'))
print(name.replace('g','simida'))
name='1,2,3,4'
b=name.split(',')
print(b)
#引号
print('today')
print("yes")
print('''OK''')
print("i'm your papa!")
'''
这是爸爸的代码
'''
print('''
heygor memda
heygor handsome
heygor cool
''')
















