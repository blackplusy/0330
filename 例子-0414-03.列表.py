#coding=utf-8
#直接输出
l1=['李元芳','钟馗','李白']
print(l1)
#遍历访问
for i in l1:
    print(i)
    print(type(i))
#成员运算访问
if '张小敬' in l1:
    print('im here!')
else:
    print('not here!!')

#列表的索引和切片
l1=['张飞','关羽','马超','云云','黄忠']
print(l1[0])
print(l1[-2])
#print(l1[5])
print(l1[2:])
print(l1[2:3])

#列表的拼接
l=[1,2,3,4]
m=['a','b']
print(l+m)

#列表的更新
l=[1,2,3]
print(l)
l[2]='柳岩'
print(l)
l[-3]='baby'
print(l)

#列表的删除
l=[1,2,3]
print(l)
del l[2]
print(l)
del l
print(l)



