#coding=utf-8

#导入webdriver模块
from selenium import  webdriver
#定义驱动
br=webdriver.Chrome()
#打开网页
br.get("https://www.taobao.com")
