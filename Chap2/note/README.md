~ 用于存放个人教程，建议使用 Jupyter Notebook 编写。

#### 基础任务
完成一个在命令行界面下天气查询程序，实现以下功能：
- 输入城市名，返回该城市最新的天气数据；
- 输入指令，获取帮助信息（一般使用h或help）；
- 输入指令，获取历史查询信息(一般使用history)；
- 输入指令，退出程序的交互（一般使用quit或exit）；

#### 基础任务实现思路
1. 获取信息：
- 通过API接口获取信息。要确定API一般接受什么输入，返回什么数据？
- 如何选择API接口。
    - 是否有Python的demo?
    - 使用上有哪些限制？
    - 数据源是否可靠？
    - 是否易于使用？
    - 课堂提供3中API：
    1. [心知天气](https://www.seniverse.com/)
    2. [Weather API](http://openweathermap.org/api)
    3. [彩云天气](http://wiki.swarma.net/index.php/%E5%BD%A9%E4%BA%91%E5%A4%A9%E6%B0%94API/v2)
- 选择 [心知天气](https://www.seniverse.com/)的API获取它提供的天气信息。
- 免费版可以获取内容：天气现象文字、代码和气温。

2. 查找API接口文档，学习使用API接口获取数据。
    - 阅读**心知天气**API[接口文档](https://www.seniverse.com/doc)，获取使用方法。

3. 使用API获取天气信息。
- 参考心知天气提供的[代码示例](https://github.com/seniverse/seniverse-api-demos)
- 修改API示例代码，使其适用于自己的情况。
- 搭建最基本的天气信息获取框架。
- 获取一个位置的天气，分析信息。获取信息如下：
```
{"results": [{"location": {"id": "WTW3SJ5ZBJUY", "name": "上海", "country": "CN", "path": "上海, 上海, 中国", "timezone": "Asia/Shanghai","timezone_offset": "+08:00"},
"now": {"text": "多云", "code" :"4","temperature": "29"}, "last_update": "2017-08-21T21:53:00+08:00"}
]}
```
- 将JSON数据转换为Python数据。
- 从获得的信息中，得到需要的信息：
    - 1. 从key-location中获得value；
    {"id": "WTW3SJ5ZBJUY", "name": "上海", "country": "CN", "path": "上海, 上海, 中国", "timezone": "Asia/Shanghai","timezone_offset": "+08:00"}
    - 2. 从第一步中的value中提取key-path的信息；
    - 3. 从key-now中获得value;
    {"text": "多云", "code" :"4","temperature": "29"}, "last_update": "2017-08-21T21:53:00+08:00"}
    - 4.从第三步获得的value中提取key-text、key-code、key-temperature、key-last-update信息。
4. 依据CH1已经实现的功能，修改main()函数结构


#### 进阶任务实现思路
- 任务: 自动更新天气
- 实现步骤：
1. 使用sched、time类，实现任务的队列和定时
2. 设计一个任务分支，一条分支对应单次查询，每次查询需要输入城市名；另一条分支对应自动查询，在输入正确城市名之后，每2小时自动更新一条天气信息



