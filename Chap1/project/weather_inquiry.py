# -*- coding:utf-8 -*-
def load_data(filename):
    city_weather = {}
    with open(filename,'r',encoding = 'utf-8') as f:
        for word in f.readlines():
            [city,weather] = word.strip().split(r',')
            city_weather[city] = weather
    return city_weather

def help():
    print('''
    \t输入城市名，查询该城市的天气.
    \t输入help，获取帮助文档.
    \t输入history，获取查询历史.
    \t输入quit，退出天气查询系统.''')

def weather_inquired(city,user_weather,city_weather):   
    user_weather[city] = city_weather.get(city)
    print(city,":",city_weather[city])
    return user_weather


def show_info(user_weather):
    for city,weather in user_weather.items():
        print(city ,':', weather)


def main():
    user_weather = {}
    city_weather = load_data('../resource/weather_info.txt')
    while True:
        user_input = input("请输入指令或你要查询的城市名:")
        if user_input in city_weather.keys():
            user_weather = weather_inquired(user_input,user_weather,city_weather)
        elif user_input == 'quit':
            print("所有查询过的城市和天气:")
            show_info(user_weather)
            exit(0)
        elif user_input == 'history':
            print("已经查询过的城市和天气:")
            show_info(user_weather)
        elif user_input == 'help':
            help()
        else:
            print("没有查询城市的天气")
   
#main()
if __name__ =='__main__':
    main()