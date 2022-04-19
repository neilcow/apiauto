import requests

# 发送 post请求
url = 'http://localhost:500/login'
requests.post(url)

# 发送headers 请求头
url = 'http://localhost:500/login'
headers = {'token': '123445'}
requests.post(url, headers=headers)


# 如何传递参数  ，
data = {'username': 'admin'}

# 传递参数2： 表单形式 , 用data=
form_data = {'form_admin': 'test1'}
# 传递参数3：json  用json=
json_data = {'json_data': 'test2'}
res = requests.post(url, json=json_data, headers=headers, params=data)

# 获取相应文本，得到的数据类型，string
print(res.text)

# 获取二进制形式
print(res.content)

# json,得到的是字典数据类型
print(res.json())

