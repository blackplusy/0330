#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
br=webdriver.Chrome()
#拖拽1
# br.get("https://www.baidu.com")
# source=br.find_element_by_link_text("新闻")
# target=br.find_element_by_link_text("地图")
# ActionChains(br).drag_and_drop(source,target).perform()
#拖拽2
br.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
br.maximize_window()
br.switch_to.frame('iframeResult')
source=br.find_element_by_id("draggable")
target=br.find_element_by_id("droppable")
actions=ActionChains(br)
actions.drag_and_drop(source,target)
actions.perform()