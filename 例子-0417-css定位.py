#coding=utf-8
from selenium import  webdriver
br=webdriver.Chrome()
br.get("https://www.baidu.com")
#1.标签选择器
# br.find_element_by_css_selector("input").send_keys("aaa")
#2.id选择器
# br.find_element_by_css_selector("#kw").send_keys("黑哥一笑百媚生")
#3.class定位
# br.find_element_by_css_selector(".s_ipt").send_keys("么么哒")
#4.其他属性定位
# br.find_element_by_css_selector("[name='wd']").send_keys("aaa")
#1.id组合属性
# br.find_element_by_css_selector('input#kw').send_keys("kouniqwa")
# 2.class组合属性
# br.find_element_by_css_selector("input.s_ipt")
#3.其他属性组合
# br.find_element_by_css_selector("input[name='wd']").send_keys("simida")
#4.只有属性名，没有值定位
# br.find_element_by_css_selector("input[name]").click()
#5.两个其他属性组合定位
# br.find_element_by_css_selector("[name='wd'][autocomplete='off']").send_keys("odusang")
#6.模糊匹配属性定位
#61.匹配属性值为字符串开头的方法
# br.find_element_by_css_selector("input[class^=s_]").send_keys("simida")
#62.匹配属性值为字符串结尾的方法
br.find_element_by_css_selector("input[class$='ipt']").send_keys("miao")
#注意 ^代表以...开头  $代表以...结尾
#7.层级定位
br.find_element_by_css_selector("#form>span>input").send_keys("aaa")
