#coding=utf-8
from  selenium import webdriver
from selenium.webdriver.support.select import Select
br=webdriver.Chrome()
br.get("http://127.0.0.1/2.html")
#实例化select类对象
selector=Select(br.find_element_by_id("selectdemo"))
#1.通过索引进行选择，索引从0开始
# selector.select_by_index("2")
#2.通过value属性进行选择
# selector.select_by_value("204")
#3.通过标签显示的text进行选择
selector.select_by_visible_text("篮球运动员")

