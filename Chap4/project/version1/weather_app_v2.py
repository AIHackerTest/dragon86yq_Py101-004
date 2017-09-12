from flask import Flask, request, render_template
from  weather_api import  retrieve_json_weather
from store_retrieve_db import create_db, store_db, retrieve_db, update_weather
import time

app = Flask(__name__)
weather_history = []
start = 0
start_time = 0

@app.route('/')
def index():
     return render_template('base_index.html')


@app.route('/user', methods=['GET', 'POST'])
def weather_app(): 
    global start
    global start_time
    user_city = request.args.get('city')
    cmd = request.args.get('action')
    try: 
        if  start==0 :
            if cmd == u'查询':
                start_time = time.clock()
                weather_info = retrieve_json_weather(user_city)
                store_db(weather_info)
                start = 1
                weather_reault = u'{weather_info[0]} {weather_info[1]}：{weather_info[2]}度，\
                            {weather_info[3]}，{weather_info[4]}，湿度{weather_info[5]}'.format(weather_info=weather_info)
                weather_history.append(weather_reault)
                return render_template('weather.html', weather_info=weather_info)
        else:
            if cmd == u'查询':
                interval = time.clock() - start_time
                if(interval < 300):
                    weather_info = retrieve_db(user_city)
                else:
                    weather_info = retrieve_json_weather(user_city)
                    store_db(weather_info)  
                    start = 0       
                weather_reault = u'{weather_info[0]} {weather_info[1]}：{weather_info[2]}度，\
                            {weather_info[3]}，{weather_info[4]}，湿度{weather_info[5]}'.format(weather_info=weather_info)
                weather_history.append(weather_reault)
                return render_template('weather.html', weather_info=weather_info)
    except KeyError as e: #当retrieve_json_weather()输入参数非法时，捕获该错误
        if cmd == u'帮助':
           return render_template('help.html')
        elif cmd == u'历史':
            return render_template('history.html', weather_history=weather_history)
        elif cmd == u'更正':
            #weather_status = user_city.split(' ')
            #update_weather(weather_status)
            #return render_template('weather_update.html')
            return render_template('help.html')
        else:
            return render_template('404.html')



if __name__ == '__main__':
    create_db()
    app.run(debug=True)