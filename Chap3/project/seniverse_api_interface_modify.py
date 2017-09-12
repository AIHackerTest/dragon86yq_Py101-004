import requests
import time
import sched

class weatherfetch(object):
    weather_all = {}
    KEY = '832fbfa10cba418596a92e7dae682a5a' 
    API = 'https://free-api.heweather.com/v5/weather' 
    LANGUAGE = 'zh-cn'
    LOCATION = 'beijing'
    commands = {'help': 1, 'h': 2, 'history': 3, 'quit':4, 'exit': 5}

    def __init__(self,city):
        self.city = city

    def get_api_data(self):
        results = requests.get(weatherfetch.API,\
                               params= {'key': weatherfetch.KEY,
                                        'city':  self.city,
                                        'lang' : weatherfetch.LANGUAGE})
        json_result = results.json()
        return json_result

    def retrieve_json_weather(self):
        json_result = self.get_api_data()
        weather_info = {}
        retrieve_data = json_result['HeWeather5'][0]
        status = retrieve_data['status']
        if status != 'ok':
            return False,None
        else:
            city = retrieve_data['basic']['city']
            weather_status = retrieve_data['now']['cond']['txt']
            wind = retrieve_data['now']['wind']
            humidity = retrieve_data['now']['hum']
            temperature = retrieve_data['now']['tmp']
            weather_info[city] = [temperature,weather_status,wind,humidity]
            return city, weather_info

    def show_weahter(self,weather_data):
        for city, data in weather_data.items():
            #print(city," ","温度:",data[0],"天气:",data[1],"风向:",data[2].get('dir'),\
                  #"风力等级",data[2].get('sc'),"湿度:",data[3])
            print("%s  温度:%s, 天气:%s, 风向:%s, 风力等级:%s, 湿度:%s" %\
                  (city,data[0],data[1],data[2].get('dir'),data[2].get('sc'),data[3]))

    def history_data(self,city, weather_data):
        self.weather_all[city] = weather_data[city]
        
    def help():
        print('''
            \t输入城市名，查询该城市的天气.
            \t输入help，获取帮助文档.
            \t输入history，获取查询历史.
            \t输入quit，退出天气查询系统
            ''')

def get_weather(cmd, wf):
    get_cmd = wf.commands.get(cmd)
    if get_cmd in [1,2]:
        wf.help()
    elif get_cmd in [4,5]:
        wf.show_weahter(wf.weather_all)
        exit(0)
    elif cmd == 3:
        wf.show_weahter(wf.weather_all)
    else:
        city, weather_info =  wf.retrieve_json_weather() 
        if city == False:
            print("请重新输入查询城市")
        else:
            wf.show_weahter(weather_info)
            wf.history_data(city,weather_info) 


def hint():
    print("""
            - 输入城市名，返回该城市最新的天气数据；
            - 输入指令，获取帮助信息（一般使用h或help）；
            - 输入指令，获取历史查询信息(一般使用history)；
            - 输入指令，退出程序的交互（一般使用quit或exit）；
            - 输入"1"每2小时自动查询输入城市的天气，输入"2"单次查询输入城市天气
            - 输入switch切换定时自动更新""")



def run_function(interval_time, cmd, wf):
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(interval_time,2,get_weather,(cmd, wf))
    print("当前时间:",time.strftime("%Y-%m-%d %X",time.localtime(time.time())))
    schedule.run()


def main():
    hint()
    auto = 0
    while True:       
        auto = input("自动定时更新请输入1，单次查询请输入其他任意字符, 退出请输入quit: ")
        if auto == 'quit':
            exit(0)
        elif auto == '1':
            print("**退出自动更新请按**: Ctrl-C \n") 
            cmd = False
            auto_interval = input("请在1-12小时之间输入需要定时更新的时间间隔: ")
            while cmd== False:
                cmd = input("请输入查询城市: ")
                wf = weatherfetch(cmd)
                cmd, weather_info = wf.retrieve_json_weather()
            while True:
                try:
                    run_function(int(auto_interval), cmd, wf)
                except KeyboardInterrupt as e:
                    print("退出自动更新")
                    break
        else:
            while True:       
                cmd = input("请输入命令或查询城市: ")
                if cmd == 'switch':
                    break
                else: 
                    wf = weatherfetch(cmd)
                    get_weather(cmd, wf)    




if __name__ == '__main__':
    main()



     





































