# 已知实时天气预报API接口为：
#    http://www.weather.com.cn/data/sk/101110101.html
#   返回的是JSON格式的数据，请爬取天气预报信息，并将爬取到的信息保存到文件中。

import json
from urllib import request

url = "http://www.weather.com.cn/data/sk/101110101.html"

if __name__ == '__main__':
    resp = request.urlopen(url)   # 发送GET请求，返回响应对象
    if resp.status == 200:
        weather_str = resp.read().decode()   # 获取响应中的内容
        weather_dict = json.loads(weather_str)  # 将字符串转换为字典
        city = weather_dict["weatherinfo"]["city"]  # 获取城市名称
        temp = weather_dict["weatherinfo"]["temp"]  # 获取温度
        with open("./data/weather_info.txt",'w',encoding="utf-8") as f:
            f.write("城市："+city+"\n")
            f.write("温度："+temp)
            print("保存成功！")

