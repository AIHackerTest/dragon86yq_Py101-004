import requests
from utils.const_value import *
import json
import time
import sched

def fetchWeather(location):
    try:
        result = requests.get(API, params={
                 'key': KEY,
                 'location': location,
                 'language': LANGUAGE,
                 'unit': UNIT
                }, timeout= 1)
        result.raise_for_status()
        return result.text
    except: 
        print("输入的城市不存在，请确认之后输入")
        return fetchWeather(get_user())

def get_info(results):
    get_weather = {}
    results = json.loads(results)
    get_info = results['results'][0]
    city = get_info['location']['name']
    temperature = get_info['now']['temperature']
    weather = get_info['now']['text']
    last_update = get_info['last_update']
    get_weather[city] = [temperature, weather, last_update]
    return get_weather,city


def help():
    print('''
    \t输入城市名，查询该城市的天气.
    \t输入help，获取帮助文档.
    \t输入history，获取查询历史.
    \t输入quit，退出天气查询系统.''')

def hint():
    print("""
        - 输入城市名，返回该城市最新的天气数据；
        - 输入指令，获取帮助信息（一般使用h或help）；
        - 输入指令，获取历史查询信息(一般使用history)；
        - 输入指令，退出程序的交互（一般使用quit或exit）；""")

def get_user():
    return input('请输入需要查询的天气：')   

def history_info(city,weather_info,store_info):
    store_info[city] = weather_info[city]
    return store_info


def show_info(user_weather):
    for city, other_info in user_weather.items():
        print("查询城市:",city, ", 气温:",other_info[0], ", 天气:",other_info[1], ", 更新时间:",other_info[2])
    
def main():     
    inquiry_weather = {}
    store_info = {}
    hint()
    while True:
        user_input = get_user()
        if user_input in ['quit','exit']:
            if not inquiry_weather:
                print("没有输入过查询的城市")
                continue
            else:
                print("所有查询过的城市和天气：")
                show_info(inquiry_weather)
                exit(0)
        elif user_input in ['help','h']:
            help()
        elif user_input == 'history':
            if not inquiry_weather :
                print("没有输入过查询的城市")
                continue
            else:
                print("已经查询过的城市和天气：")
                show_info(inquiry_weather)
        else:
            results= fetchWeather(user_input)
            get_weather,city = get_info(results)
            show_info(get_weather)
            inquiry_weather = history_info(city,get_weather,store_info)


if __name__ == '__main__':
    main()






