#coding=utf-8
import unittest
class TestStingMethod(unittest.TestCase):
    #测试用例1：判断foo大写之后是否和FOO相等
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    #测试用例2:判断Foo是否是大写
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
    #测试用例3:判断字符串通过split拆分后是否是['hello','world']
    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])

if __name__=='__main__':
    unittest.main()