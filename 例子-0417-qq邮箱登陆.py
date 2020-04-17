#coding=utf-8
from selenium import webdriver
import time
br=webdriver.Chrome()
br.get("https://mail.qq.com/")
time.sleep(3)
br.switch_to.frame("login_frame")
br.find_element_by_link_text("帐号密码登录").click()
br.find_element_by_id("u").send_keys("aaa")
time.sleep(2)
# br.switch_to.default_content()
br.switch_to.parent_frame()
br.find_element_by_id("wxLoginTab").click()
