#! python3
# quickWeather.py - 从命令行输入位置参数，从OpenWeatherMap获取近三天天气数据
 
import sys,requests,json
 
# 获取命令行参数
print(sys.argv[0])
# if len(sys.argv) < 2:
#     print('缺少位置信息')
#     sys.exit()
 
location = ''.join(sys.argv[1:])
location = 'Milwaukee'
# 从网站获取数据(key几个小时后失效)
appid = '47a564656ff9e7f0001a0a15a0b9b3ba'
response = requests.get(r'http://api.openweathermap.org/data/2.5/find?q=%s&cnt=3&lang=zh_cn&units=metric&APPID=%s' % (location,appid))

# response = requests.get(r'http://api.openweathermap.org/data/2.5/weather?q=%s&lang=zh_cn&units=metric&APPID=%s'% (location,appid))
response.raise_for_status()
 
# 加载并打印json数据
weatherData = json.loads(response.text)
info = weatherData['list']
address = info[0]['name']

tomorrow = info[1]['weather'][0]['description']

tem_min = int(info[0]['main']['temp_min'])
tem_max = int(info[0]['main']['temp_max'])
today = info[0]['weather'][0]['description']
# weatherData['name']
# weatherData['main']['temp']

print('''
    %s的天气状况：
        今天：%s
        明天：%s'''%(address,today,tomorrow))