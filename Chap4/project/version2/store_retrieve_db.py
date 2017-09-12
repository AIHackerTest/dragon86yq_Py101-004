import sqlite3

def create_db():
    conn = sqlite3.connect('weather_information.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS weather (update_time, city, temperature, weather_status, wind_dir, humidity)')
    conn.commit()
    conn.close()

def store_db(weather_info):
    conn = sqlite3.connect('weather_information.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO weather VALUES (?,?,?,?,?,?)',(weather_info))
    conn.commit()
    conn.close()

def retrieve_db(city):
    conn = sqlite3.connect('weather_information.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM weather WHERE city=?",(city,))
    weahter_retrieve = cur.fetchone()
    conn.commit()
    conn.close()
    return weahter_retrieve

def update_weather(argvs):
    conn = sqlite3.connect('weather_information.db')
    cur = conn.cursor()
    cur.execute("UPDATE weather SET weather_status=? WHERE city=?",(argvs[1],argvs[0],))
    #cur.execute("SELECT * FROM weather WHERE city=?",(argvs[0],))
    #weather_update = cur.fetchone()
    conn.commit()
    conn.close()
    #return weather_update