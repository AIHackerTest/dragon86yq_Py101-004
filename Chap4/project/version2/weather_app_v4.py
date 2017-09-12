from flask import Flask, request, render_template
from  weather_api import  retrieve_json_weather
from store_retrieve_db import create_db, store_db, retrieve_db, update_weather
import time

app = Flask(__name__)
weather_history = []
start = 1  #用于判断直接调用API，或者从数据库中获取数据。1：直接调用API；0：从数据库取数据
start_time = 0 #用于记录第一次点击查询的时间

@app.route('/')
def index():
     return render_template('base_index.html')

def show_info(weather_info):
    return u'{weather_info[0]} {weather_info[1]}：{weather_info[2]}度, {weather_info[3]}, {weather_info[4]}，湿度{weather_info[5]}'.format(weather_info=weather_info)

# 2次点击查询的时间
def log_time(N,begin):
    interval = time.time() - begin
    if interval < (60 * N):
        return 0
    else:
        return 1

@app.route('/user', methods=['GET', 'POST'])
def weather_app(): 
    global start
    global start_time
    user_city = request.args.get('city')
    cmd = request.args.get('action') 
    if cmd == u'查询':
        if start == 1: #初始值为1，直接调用API获取数据
            start_time = time.time()
            start = log_time(5,start_time) #5分钟内多次查询，直接从数据库取数据
            weather_info = retrieve_json_weather(user_city)
            if weather_info:
                weather_reault = show_info(weather_info)
                print(weather_reault)
                weather_history.append(weather_reault)
                store_db(weather_info) #将API数据存入数据库
                return render_template('weather.html', weather_info=weather_reault)
            else:
                return render_template('404.html')
        else:
            start = log_time(5,start_time) #判断2次点击查询的时间是否在5分钟之内
            weather_info = retrieve_db(user_city)  #从数据库取数据  
            if weather_info:           
                weather_reault = show_info(weather_info)
                print(weather_reault)
                weather_history.append(weather_reault)
                return render_template('weather.html', weather_info=weather_reault)
            else:
                return render_template('4041.html')
    elif cmd == u'帮助':
        return render_template('help.html')
    elif cmd == u'历史':
        return render_template('history.html', weather_history=weather_history)
    elif cmd == u'更正': 
        weather_status = user_city.split(' ')
        update_weather(weather_status) #存入数据库
        return render_template('weather_update.html')
    else:
        return render_template('help.html')
    


if __name__ == '__main__':
    create_db()
    app.run(debug=True)