# -*- coding: utf-8 -*-  
import requests
import json
import itchat
from itchat.content import *


class Infomation(object):
    def __init__(self):
        self.city = ""

    def getWeather(self):
        r=requests.get('http://www.weather.com.cn/data/sk/101190101.html')
        r.encoding='utf-8'
        data = r.json()
        self.city = data['weatherinfo']['city']
        self.temperature = data['weatherinfo']['temp']
        self.humidity = data['weatherinfo']['SD']
        return "城市: %s, 温度: %s, 湿度: %s" % (self.city, self.temperature, self.humidity)


    def getOutIP(self):
        r=requests.get('http://pv.sohu.com/cityjson')
        data = r.text.split('=')[1]
        jdata = json.loads(data[:-1])
        self.outIp = jdata['cip']
        return self.outIp


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    info = Infomation()
    if msg.text == 'ip':
        msg.user.send('IP: %s' % (info.getOutIP()))
    elif msg.text == 'weather':
        msg.user.send(info.getWeather())
    else:
        msg.user.send('Not supported')


if __name__ == "__main__":
    itchat.auto_login(enableCmdQR=True)

    itchat.send('Hello, filehelper', toUserName='filehelper')

    author = itchat.search_friends(nickName='Zlatan500')[0]
    author.send('greeting, littlecoder!')
    itchat.run()
