# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:26:49 2018

@author: lenovo
"""

##测试七天的天气解析
city=input('输入城市名称：')
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
data=json.loads(info)
print('未来四天的天气是如下：')
for i in range(4):
    print('第'+str(i+1)+'天的天气：\n')
    print(data['list'][(i+1)*8-1]['dt_txt']+'  天气：'+data['list'][(i+1)*8-1]['weather'][0]['description']+'  温度：'+str(data['list'][(i+1)*8-1]['main']['temp'])+'华氏度'+'  气压：'+str(data['list'][(i+1)*8-1]['main']['pressure'])+'\n')
