# 单元测试 unittest
"""
断言
assert
如果断言失败，抛出异常，如果成功，正常运行
"""
import requests


url = 'http://localhost:5000/login'
data = {"mobliephone": '13112341234', 'pwd': '123456'}
headers = {'X-Media-Type': 'test.v2'}


def visit(url, data, headers):
    res = requests.post(url, json=data, headers=headers)


assert 1 + 2 == 3
print('assert finished')
