#coding=utf-8
import csv
#csv文件读
with open('D:\\1.csv','r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)
        print(type(i))
#csv文件写
with open('D:\\100.csv','w') as f:
    file=csv.writer(f,dialect='excel')
    # 写入方式使用writerow
    file.writerow([1,2,3,4])
    file.writerow([5,6,7,8])

print('ok了')