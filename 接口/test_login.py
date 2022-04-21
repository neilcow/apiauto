"""
1、模块名，以test开头
2、类名以Test开头
3、方法 test开头
4、继承unittest.TestCase
5、运行测试用例 使用unittest

6、断言结果
. 表示通过，或者pass
F  False，表示断言没有通过
E Error 表示程序内部发生错误

"""
import unittest
from 接口.d4_unittest import visit

url = 'http://localhost:5000/login'
data = {"mobliephone": '13112341234', 'pwd': '123456'}
headers = {'X-Media-Type': 'test.v2'}


# 继承unittest.TestCase
class TestLogin(unittest.TestCase):
    def test_login_success(self):
        # res = visit(url, data, headers)
        # print(res)
        try:
            self.assertEqual(1, 3-2)
        except AssertionError as result:
            print('断言失败', result)
            raise AssertionError


if __name__== '__main__':
    unittest.main