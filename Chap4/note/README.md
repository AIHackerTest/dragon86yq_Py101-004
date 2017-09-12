~ 用于存放个人教程，建议使用 Jupyter Notebook 编写。

#### 基础任务
完成一个网页版天气查询程序，实现以下功能：
    - 基本功能
      - 输入城市名，获取该城市最新天气情况
      - 点击「帮助」，获取帮助信息
      - 点击「历史」，获取历史查询信息
    - 扩展功能
      - 使用 SQLite 存储天气数据
      - 用户可通过 Web 页面的用户更正按钮，更正天气数据到数据库
      - 如果在5分钟以内查询相同的数据, 不用通过 API 访问远程数据源
      - 可记录多个用户不同的查询历史（较难，选作）
    - 部署在命令行界面

#### 进阶任务
学有余力，可以使用 Flask 的扩展 Flask-SQLAlchemy 来替代 sqlite3 模块，和 Flask 更好地结合。

#### 内容分析
  - 难点
    - 如何与数据库进行交互
      - 如何将数据存入数据库
      - 如何从数据库提取需要的数据
    - 怎样操作数据库

  - 任务分解
    - 实现基本功能（chap2和chap3已经实现）
    - 数据库操作
      - SQL是什么
      - CRUD操作
    - 数据库交互
      - 如何与SQLite数据库建立连接？
      - 如何在SQLite中建立游标对象？
      - 如何借助游标执行SQL语句？
      - 如何将API返回的数据直接存储到数据库？

  - 任务解析
    - SQL：Structure Query Language
    - SQL基本操作：CRUD
      - C: Create
      - R: Read
      - U: Update
      - D: Delete
    - 数据库交互
      - SQLite


#### database
#####SQL 基本操作
1. SELECT
2. INSERT INTO 
3. DELETE 
4. DUPDATE

SELECT * FROM table_name;
SELECT column1, column2 FROM table_name;
SELECT DISTINCT column1, column2 FROM table_name;
SELECT column1, column2 FROM table_name WHERE condition;

INSERT INTO table_name (column1,column2)
VALUES (value1,value2);

NULL
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
WHERE column_name IS NOT NULL;

UPDATE table_name
SET column1=value1, column2=value2
WHERE condition;

##### 如何将数据存入db及从db中取出数据
1. 使用下面语句可以将数据存入db
   - cur.execute("INSERT INTO people VALUES (?,?)",(who,age))
2. 使用下面语句可以从db对应位置取出数据
   - cur.execute('SELECT * FROM people WHERE name_last=?',(who,))
   - print(cur.fetchall())
   - 需要注意参数调用


#### 资料
1. 关系型数据库和非关系型数据库(http://blog.csdn.net/robinjwong/article/details/18502195)
2. [SQLite使用](https://www.sqlite.org/cli.html)
