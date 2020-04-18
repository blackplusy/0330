#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
br=webdriver.Chrome()
br.get("https://www.baidu.com")
#单击元素
#perform() 代表执行操作
#ActionChains() 传入webdriver驱动
#click()  传入你需要点击的元素
element=br.find_element_by_link_text("新闻")
# ActionChains(br).click(element).perform()
#元素上按下左键不放手
# ActionChains(br).click_and_hold(element).perform()
#元素上单击右键
# ActionChains(br).context_click(element).perform()
#元素上双击
ActionChains(br).double_click(element).perform()



