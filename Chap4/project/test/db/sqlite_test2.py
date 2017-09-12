import sqlite3
def create_db():
    conn = sqlite3.connect('weather_information.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS weather (update_time, city, temperature, weather_status, wind_dir, humidity)')
    conn.commit()
    conn.close()

weather_info = ['2017-09-06 12:46', '北京', '31', '晴', '西南风', '24']
def insert_data_db(weather_info):
    conn = sqlite3.connect('weather_information.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO weather VALUES (?,?,?,?,?,?)',(weather_info))
    cur.execute("SELECT * FROM weather WHERE city=?",('北京',))
    weahter_retrieve = cur.fetchone()
    print(weahter_retrieve)

create_db()
insert_data_db(weather_info)