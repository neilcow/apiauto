# 一个session 一次会话对象
#
import requests

# url = 'http://localhost:5000/login'
# data = {'mobliepphone': '13112341234', 'pwd': '12345'}
# res = requests.post(url, json=data)
# print(res.json())
#
# # 获取cookie
# cookies = res.cookies
#
# recharge_url = 'http://localhost:5000/recharge'
# recharge_data = {'mobilephone': '13112341234', 'recharge': '1000'}
# res = requests.post(recharge_url, json=recharge_data, cookies=cookies)
#
# print(res.text)

# session 的使用， 相当一个浏览器，这个时候就不需要cookie,使用session管理机制，自动把cookie带上去
session = requests.Session()
url = 'http://localhost:5000/login'
data = {'mobliepphone': '13112341234', 'pwd': '12345'}
res = session.post(url, json=data)
print(res.json())

recharge_url = 'http://localhost:5000/recharge'
recharge_data = {'mobilephone': '13112341234', 'recharge': '1000'}
res = session.post(recharge_url, json=recharge_data)

print(res.text)