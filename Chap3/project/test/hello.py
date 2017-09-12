from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/user_input', method=['GET', 'POST'])
def weather_app():
    city = request.args.get('city')
    print(city)

if __name__ == '__main__':
    app.run(debug=True)


    
