#coding=utf-8
#栈的方式访问列表
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
#获取列表索引
l=['a','b','d']
print(l.index('a'))

l=['a','b','d','e']
for index,value in enumerate(l):
    print('索引是'+str(index)+'的值是：'+str(value))
#列表的排序
l=[1,2,3,4]
print(l)
l.reverse()
print(l)
l=[1,3,5,2,4,6]
print(l)
l.reverse()
print(l)
l=[1,3,5,2,4,6]
l.sort()
l.reverse()
print(l)
l=[1,3,5,2,4,6]
l.sort(reverse=True)
print(l)

#insert()
l=['a','b','c']
l.insert(1,'d')
print(l)
l.insert(-1,'aaaaa')
print(l)
#extend()
l=['a','b','c']
l.extend('d')
print(l)
l.extend([1,2,3])
print(l)


