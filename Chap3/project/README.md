~ 用于存放本周任务成果。
#### 基础任务
1. 完成一个网页版天气查询
  - 实现以下功能：
    - 基本功能
      - 输入城市名称，获取该城市最新天气情况
      - 点击[帮助]，获取帮助信息
      - 点击[历史]，获取历史查询信息
    - 部署在命令行界面
  - 附上软件使用说明README.md，能令其他同学根据说明书运行程序，使用所有功能。
2. 撰写**个人教程**，讲解相关技能点，分享自己的探索发现：
  - 实现这版程序的关键是什么？难点是什么？
    - 为什么这对你来说是难点？
    - 如何突破这个难点？
  - 完成这版程序，容易踩的坑是什么？
  - 完成这版程序，有什么通用的模式（即永久性解决所有同类问题的方法）、
3. 根据自评维度给楼上同学一些反馈。

#### 任务解析
难点：
1. 如何实现程序与网页的交互。
  - 如何发送数据到网页。
  - 如何从网页获取数据。
2. 了解web开发基础知识。
  - 什么是web开发
  - 什么是web框架，它可以干嘛？
  - 基于Python的web框架有哪些？
3. Flask框架是什么？

解析：
使用flask框架实现server和网页的交互。
  - 使用@app.route('/')装饰器触发函数，该函数返回值就是网页显示内容；
  - 使用request.args.get('key')或者request.form('key')获得html上的信息；
  - 使用render_template类可以将变量传递给hmtl，参考Jinja2用法


#### 程序说明
1. 主程序为weather_app.py
2. 在weather_app.py中调用第二周作业seniverse_api_interface_modify.py
3. template中有4个html文件，base_index.html是基文件，其他三个.html继承与base_index.html
4. 运行代码时有可能出现长时间等待，其原因是出现如下错误：GET /favicon.ico HTTP/1.1" 404 -127.0.0.1 ，该错误解决方法是添加一个静态图片，本程序暂时未解决。

#### 修改说明
在完成基本功能基础上对代码进行优化和修改：
1. 删减seniverse_api_interface_modify.py文件，保留get_api_data()，retrieve_json_weather()两个函数，并对retrieve_json_weather进行部分修改，将seniverse_api_interface_modify.py重命名为weather_api.py
2. 增加/static/img目录，用于存放静态图片
3. 增加404.html
4. [文件存放目录](https://github.com/dragon86yq/Py101-004/tree/master/Chap3/project/version2)



参考资料：
1. [flask快速入门](http://docs.jinkan.org/docs/flask/quickstart.html#redirects-and-errors)
    [flask快速入门——英文版](http://flask.pocoo.org/docs/0.12/quickstart/#quickstart)
2. [欢迎进入Flask大型教程项目](http://www.pythondoc.com/flask-mega-tutorial/templates.html#id7)
3. [Your First Flask Website](http://pythonhow.com/your-first-flask-website/)
4. [HTML](https://www.w3schools.com/html/html_elements.asp)