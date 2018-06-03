# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:26:49 2018

@author: lenovo
"""

##测试七天的天气解析
import time
huanyin=['欢','迎','使','用','天','气','预','报','a','p','p','^_^']
le=len(huanyin)
for i in range(12):
    print(huanyin[i],end="")
    time.sleep(0.2)
ju=1
while ju==1:
    city='leshan'
    city=input('输入城市名称：')
    address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
    info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
    data=json.loads(info)
    print('未来四天的天气如下：')
    for i in range(4):
        print('第'+str(i+1)+'天的天气：\n')
        print(data['list'][(i+1)*8-2]['dt_txt']+'  天气：'+
              data['list'][(i+1)*8-2]['weather'][0]['description']+'  温度：'+
              str(data['list'][(i+1)*8-2]['main']['temp'])+'华氏度'+'  气压：'+
              str(data['list'][(i+1)*8-2]['main']['pressure'])+'\n')
    ju=int(input('输入数字选择后续操作：1.继续查询 2.退出查询\n'))
    if ju==2:
        print('谢谢使用，再见！')
