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


setUp: 每次测试用例方法运行之前都会执行的，前置条件
可以把测试数据放到 setUp当中

tearDown: 每次测试用例完成后，都会执行的方法

"""
import unittest
from 接口.d4_unittest import visit

# url = 'http://localhost:5000/login'
# data = {"mobliephone": '13112341234', 'pwd': '123456'}
# headers = {'X-Media-Type': 'test.v2'}

data = {
    'url': 'http://localhost:5000/login',
    'data': {"mobliephone": '13112341234', 'pwd': '123456'},
    'headers': {'X-Media-Type': 'test.v2'}
}


# 继承unittest.TestCase
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.data = data

    def test_login_success(self):
        res = visit(self.data['url'], self.data['data'], self.data['headers'])
        self.assertEqual(self.data['expected'], res)
        # try:
        #     self.assertEqual(1, 3-2)
        # except AssertionError as result:
        #     print('断言失败', result)
        #     raise AssertionError

    def tearDown(self) -> None:
        print('测试用例执行完毕后要执行的方法')


if __name__== '__main__':
    unittest.main