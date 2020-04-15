#coding=utf-8
#1.读文件（r）
# 定义一个变量接受open函数打开文件后的内容
file=open('D:\\test.txt','r')
print(file)
for i in file:
    print(i)
file.close()
#2.写入文件
str1='o my dear baby!!'
file=open('D:\\test100.txt','w')
file.write(str1)
file.close()
print('数据已经写入完毕')
#3.追加文件
file=open('D:\\test.txt','a')
file.write('O M  ladyGaGa!\n')
file.close()
print('追加完毕')