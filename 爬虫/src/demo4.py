# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :demo4.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/19 15:10


import urllib.request,urllib.parse

def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)
    return datalist

def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"
    }

    request = urllib.request.Request(url,headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except Exception as e:

        print(e)
    return html

def saveData(savepath):
    pass


if __name__ == '__main__':
    # url = "https://movie.douban.com/top250?start="
    url = "http://www.xinfadi.com.cn/priceDetail.html"
    getData(url)
