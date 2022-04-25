"""
收集测试用例：TestLoader，加载器，加载测试用例
放到测试集合（测试套件）TestSuite

1、初始化testloader
2、suite = testloader.discover(文件夹路径, 'demo_*.py'), 第二个参数如果不写，默认是以test开头的文件
如果第二个参数写了，就是代表以这个名字demo,开头的文件
3、如果要运行用例，就要放到指定的文件夹中

TestRunner
1、运行用例
2、生成测试报告

"""
import os
import unittest
# 1、初始化testloader
from 接口 import test_login
from 接口.HTMLTestRunnerNew import HTMLTestRunner
from 接口.test_cases import test_register
from 接口.test_cases.test_recharge import TestRecharge
from 接口.test_login import TestLogin

testloader = unittest.TestLoader()

# 2、 查找测试用例，加载
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'test_cases')
suite = testloader.discover(case_path)

# 只运行某几个模块
# suite = testloader.loadTestsFromModule(test_login)
# suite2 = testloader.loadTestsFromModule(test_register)

# 只运行某几个类
# suite = testloader.loadTestsFromTestCase(TestLogin)
# suite2 = testloader.loadTestsFromTestCase(TestRecharge)


# suite3 = testloader.loadTestsFromName()

# suite_total = unittest.TestSuite()
# suite_total.addTests(suite)
# suite_total.addTests(suite2)


print(suite)


# report
report_path = os.path.join(dir_path, 'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)
# file_path = os.path.join(report_path, 'test_result.txt')
file_path = os.path.join(report_path, 'test_result.html')

# text ,对于html 一定要用二进制形式打开，wb
with open(file_path, 'wb') as f:
    # 初始化运行期，是以普通文本生成测试报告，TextTestRunner
    # runner = unittest.TextTestRunner(f, verbosity=2)
    runner = HTMLTestRunner(f)
    runner.run(suite)