# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :demo3.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/19 13:56

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.parse
import xlwt

request = urllib.request.urlopen('http://www.baidu.com')
print(request.read().decode('utf-8'))

#将爬虫伪装成网站
# url = 'https://www.douban.com'
url = 'https://douban.com'

headers = {
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"

}
# data = bytes(urllib.parse.urlencode({'name':'py'}),encoding='utf-8')
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))