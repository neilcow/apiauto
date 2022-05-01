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

from 接口.common.excel_handler import ExcelHandler
from 接口.common.requests_handler import RequestHandler
from 接口.d4_unittest import visit
from 接口.libs import ddt




# url = 'http://localhost:5000/login'
# data = {"mobliephone": '13112341234', 'pwd': '123456'}
# headers = {'X-Media-Type': 'test.v2'}

# test_data = [
#     {'url': 'http://localhost:5000/login',
#      'method': 'post',
#      'data': {"mobliephone": '13112341234', 'pwd': '123456'},
#      'headers': {'X-Media-Type': 'test.v2'},
#      'expected': 'hello world'},
#
#     {'url': 'http://localhost:5000/login',
#      'method': 'post',
#      'data': {"mobliephone": '123456', 'pwd': '123'},
#      'headers': {'X-Media-Type': 'test.v2'},
#      'expected': 'hello world'}
# ]

# 从excel中读取数据
test_data = ExcelHandler(r'd:\cases.xlsx').read('Sheet1')
print(test_data)


# 继承unittest.TestCase
@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @ddt.data(*test_data)
    # 将*test_data当中的一组测试数据，赋值到data_info这个参数，相当for循环
    # 注意需要把读取的字符串格式转成字典格式
    def test_login_success(self, data_info):
        res = RequestHandler().visit(data_info['method'],
                                   data_info['url'],
                                   json=eval(data_info['data']),
                                   headers=eval(data_info['headers']))
        self.assertEqual(res['msg'], self.data['expected'])
        # try:
        #     self.assertEqual(1, 3-2)
        # except AssertionError as result:
        #     print('断言失败', result)
        #     raise AssertionError

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
