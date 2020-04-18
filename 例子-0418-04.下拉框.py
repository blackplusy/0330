#coding=utf-8
from  selenium import webdriver
br=webdriver.Chrome()
br.get("http://127.0.0.1/1.html")
#1.通过send_keys()
# br.find_element_by_id("select").send_keys("闽南话")

#2.通过二次操作
br.find_element_by_id("select").find_element_by_xpath("//option[@value='30']").click()