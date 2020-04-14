#coding=utf-8
tup=(1)
print(tup)
print(type(tup))

tup=(2,)
print(type(tup))

#访问元组
a=(1,2,3)
print(a)

for i in a:
    print(i)

if 3 in a:
    print('yes')

#删除元组
a=(1,2,3)
del a

#print(a)
#索引和切片
tup=(1,2,3,4,5)
print(tup)
print(tup[0])
print(tup[-2])
print(tup[2:4])
print(tup[3:])
print(tup[:3])

#补充
tup=(1,2,3,4,5)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(3))
print(tup.count(3))












