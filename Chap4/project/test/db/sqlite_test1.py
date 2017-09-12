#将数据通过变量存入db
#通过变量从db中获取数据
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table people (name_last, age)")
who = "Yeltsin"
age = 72
cur.execute("INSERT INTO people VALUES (?,?)",(who,age))
cur.execute('SELECT * FROM people WHERE name_last=? AND age=?',(who,age,))
print(cur.fetchall())
cur.execute("select * from people where name_last=:who and age=:age",
            {"who":who,"age":age})

#
http://www.philvarner.com/test/ng-python3-db-api/


