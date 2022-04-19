import requests

# 一、get 请求
# url = 'http://api.github.com'
# res = requests.get(url)
# print(res.text)

# 如何传递参数，如何修改请求头，token
# headers = {'token': '1234', 'username': 'test'}
# url = 'http://localhost:5000/login'
# res = requests.get(url, headers=headers)
# print(res.text)

# 如何传递参数，位置参数，或者关键字参数 params，是通过query_string 的形式传递的
data = {'name': 'admin', 'pwd': '123456'}
headers = {'token': '1234', 'username': 'test'}
url = 'http://localhost:5000/login'
res = requests.get(url, params=data, headers=headers)
print(res.text)





