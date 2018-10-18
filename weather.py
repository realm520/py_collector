# -*- coding: utf-8 -*-  
import requests
import json

r=requests.get('http://www.weather.com.cn/data/sk/101190101.html')
r.encoding='utf-8'
print("city:"+ r.json()['weatherinfo']['city'],"\nwendu:"+r.json()['weatherinfo']['temp'],"\nshidu:"+r.json()['weatherinfo']['SD'])

r=requests.get('http://pv.sohu.com/cityjson')
data = r.text.split('=')[1]
jdata = json.loads(data[:-1])
print(jdata['cip'])
