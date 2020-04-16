#coding=utf-8

from selenium import webdriver
br=webdriver.Chrome()
br.get("https://www.baidu.com")
#1.通过id的值进行元素的定位(id="kw")
# br.find_element_by_id("kw").send_keys("黑哥一笑,世事难料！")
# br.get("https://www.taobao.com")
# br.find_element_by_id('q').send_keys("黑哥")
#2.通过class进行定位(class="s_ipt")
# br.find_element_by_class_name("s_ipt").send_keys("李子柒")
#3.通过tag定位(有可能定位不到)
# br.find_element_by_tag_name("input").send_keys("memeda")
#4.通过link定位
# br.find_element_by_link_text("hao123").click()
#5.通过partial_link定位
# br.find_element_by_partial_link_text("闻").click()
#6.xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("么么哒")
# br.find_element_by_xpath("//*[@autocomplete='off']").send_keys("kouniqiwa")
#7.css定位
# br.find_element_by_css_selector("#kw").send_keys("oyeah!!!")
#8.通过name进行定位
br.find_element_by_name("wd").send_keys("haleshao!")
br.find_element_by_id("su").click()
