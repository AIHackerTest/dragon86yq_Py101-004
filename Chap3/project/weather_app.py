from flask import Flask, request, render_template
from  seniverse_api_interface_modify import weatherfetch, get_weather
app = Flask(__name__)


@app.route('/')
def index():
     return render_template('base_index.html')

@app.route('/user', methods=['GET', 'POST'])
def weather_app():
        user_city = request.args.get('city')
        cmd = request.args.get('action')
        wf = weatherfetch(user_city)
        city, weather = wf.retrieve_json_weather()
        if cmd == u'查询':        
            if city == False:
               return render_template('weather.html', weather=weather)
            else:
                wf.history_data(city, weather)
                return render_template('weather.html', weather=weather)
        elif cmd == u'帮助':
           return render_template('help.html')
        elif cmd == u'历史':
            weather_history = wf.weather_all
            return render_template('history.html', weather_history=weather_history)


if __name__ == '__main__':
    app.run(debug=True)