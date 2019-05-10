* 【Python】利用网站API接口获取天气信息[link](https://blog.csdn.net/Kimidake/article/details/85054210) 
  * 从OpenWeatherMap获取近三天天气数据
  * http://api.openweathermap.org/data/2.5/weather?q=Milwaukee&APPID=47a564656ff9e7f0001a0a15a0b9b3ba  
* Python使用免费天气API,获取全球任意地区的天气情况  [link](https://blog.csdn.net/dongyouyuan/article/details/79475143)
* Python使用免费天气API,获取全球任意地区的天气情况 [link](https://blog.csdn.net/dongyouyuan/article/details/79475143)

 

[http://t.weather.sojson.com/api/weather/city/101030100](http://t.weather.sojson.com/api/weather/city/101030100) 



### Units format

##### Description:

Standard, metric, and imperial units are available. 

##### Parameters:

**units** metric, imperial. When you do not use units parameter, format is Standard by default. 

Temperature is available in Fahrenheit, Celsius and Kelvin units. 

- For temperature in Fahrenheit use units=imperial
- For temperature in Celsius use units=metric
- Temperature in Kelvin is used by default, no need to use units parameter in API call

List of all API parameters with units [openweathermap.org/weather-data](http://openweathermap.org/weather-data)

##### Examples of API calls:

standard [api.openweathermap.org/data/2.5/find?q=London](http://samples.openweathermap.org/data/2.5/find?q=London&appid=b6907d289e10d714a6e88b30761fae22)

metric [api.openweathermap.org/data/2.5/find?q=London&units=metric](http://samples.openweathermap.org/data/2.5/find?q=London&units=metric&appid=b6907d289e10d714a6e88b30761fae22)

imperial [api.openweathermap.org/data/2.5/find?q=London&units=imperial](http://samples.openweathermap.org/data/2.5/find?q=London&units=imperial&appid=b6907d289e10d714a6e88b30761fae22)