import requests
from utils.const_value import *
import json
import time
import sched
import sys

fixed_time = 60*60*2 #单位秒
debug_time = 10 #10秒

def fetchweather(location):
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
        #exit(0)
        return fetchweather(get_user())

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
        - 输入指令，退出程序的交互（一般使用quit或exit）；
        - 输入"1"每2小时自动查询输入城市的天气，输入"2"单次查询输入城市天气""")

def get_user():
    return input('请输入需要查询的天气：')   

def history_info(city,weather_info,store_info):
    store_info[city] = weather_info[city]
    return store_info


def show_info(user_weather):
    for city, other_info in user_weather.items():
        print("查询城市:",city, ", 气温:",other_info[0], ", 天气:",other_info[1], ", 更新时间:",other_info[2])
    
def get_all_info(user_input,store_info):     
    if user_input in ['quit','exit']:
        if not store_info:
            print("没有输入过查询的城市")
            #continue
        else:
            print("所有查询过的城市和天气：")
            show_info(store_info)
            exit(0)
    elif user_input in ['help','h']:
        help()
    elif user_input == 'history':
        if not store_info :
            print("没有输入过查询的城市")
            #continue
        else:
            print("已经查询过的城市和天气：")
            show_info(store_info)
    else:
        results= fetchweather(user_input)
        get_weather,city = get_info(results)
        show_info(get_weather)
        history_info(city,get_weather,store_info)
 

def run_function(location,store_info1):
    print("当前时间:",time.strftime("%Y-%m-%d %X",time.localtime(time.time())))
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(0, 2, get_all_info,(location,store_info1))   
    schedule.run()


def timer(location,store_info1):   
    print("如果要退出请按: Ctrl-C")
    while True:
        run_function(location, store_info1)
        time.sleep(debug_time)


if __name__ == '__main__':
    store_info1 = {}
    hint()
    try:
        auto = input("请输入--  输入1每2小时自动查询一次,输入其他单次查询：")
        if auto == '1':
            user_input_auto = get_user()
            results= fetchweather(user_input_auto)
            get_weather,city = get_info(results)
            timer(city, store_info1)
        else:
            while True:
                user_input = get_user()
                get_all_info(user_input,store_info1)
    except KeyboardInterrupt as e:
        print("退出程序")
        exit(0)


