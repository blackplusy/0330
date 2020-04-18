#coding=utf-8
from  selenium import webdriver
import time
br=webdriver.Chrome()
#1.定位上传按钮，添加本地文件
# br.get("http://127.0.0.1/3.html")
# time.sleep(2)

# br.find_element_by_name("file").send_keys("D:\\1.txt")
# time.sleep(2)
#2.文件的下载
br.get("https://pypi.org/project/selenium/3.6.0/#files")
time.sleep(2)
br.find_element_by_link_text("selenium-3.6.0.tar.gz").click()
time.sleep(10)
print('ok')