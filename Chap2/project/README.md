#### 实时天气查询程序

#### 基础任务
完成一个在命令行界面下天气查询程序，实现以下功能：
- 输入城市名，返回该城市最新的天气数据；
- 输入指令，获取帮助信息（一般使用h或help）；
- 输入指令，获取历史查询信息(一般使用history)；
- 输入指令，退出程序的交互（一般使用quit或exit）；

##### 函数说明
1. fetchWeather: 获取心知天气提供的天气数据
参数:
- input
    - location: 需要查询的城市名称可以是中文或者拼音
- return
    - result.text，从心知天气获取的城市天气信息，数据类型json

2. get_info: 将获取的json类型数据转为Python使用数据，并提取天气信息
参数:
- input
    - results: 从心知天气获得的天气数据，函数fetchWeather的返回值
- return:
    - get_weather: 解析出来的天气信息，字典类型，含有：城市、温度、天气、更新时间
    - city: 查询的城市

3. help(): 输出帮助信息

4. hint(): 输出提示信息

5. get_user: 输入需要查询的城市

6. history_info: 保存所有输入的城市和天气
参数: 
- input
    - city: 查询的城市
    - weather_info: 查询城市对应的天气，字典类型
    - store_info: 保存历次输入的城市和天气，字典类型
- return
    - 保存所有输入的城市和天气

7. show_info: 显示查询城市的天气

8. main: 主函数

#### 进阶任务
1. 在之前输入城市名时查询天气，有没有可能制定时间，让程序定时查询天气？
2. 选一个国内API和国外API分别进行调用，了解不同的调用姿势。
##### 函数说明
新增函数和修改函数
1. 将基本功能中main()函数修改为函数get_all_info，实现功能：根据输入的城市显示天气，并存储输入的城市以及天气
2. run_function和timer两个函数一起实现定时执行函数get_all_info功能
3. 增加一个输入判断：判断单次查询天气，还是自动更新天气

参考资料：
1.  [心知天气](https://www.seniverse.com/)
2. [心知天气API参考代码](https://github.com/seniverse/seniverse-api-demos)

3. 国外的天气API[Apixu API](https://www.apixu.com/)
4. [Apixu API参考代码](https://github.com/apixu/apixu-python)


#### 代码优化说明
1. [代码地址]()
2. 功能说明
创建一个类weatherfetch，从和风天气API获取信息，解析获取的信息，显示解析出来的信息，保存历次查询的信息。
weatherfetch类主要属性有：
    - weather_all
      作用：保存每次查询的信息，字典类型，key对应查询城市，value对应查询天气。
    - city
      作用：需要查询的城市，例化weatherfetch时需要设置参数该参数

weatherfetch类主要函数有：
    - get_api_data()
      参数：无
      作用：获取和风天气API信息
      返回值：获取的天气信息，数据类型json
    - retrieve_json_weather()
      参数：无
      作用：从获取的信息中解析出查询的城市，天气，温度，风向，风力等级，湿度信息
      返回值：查询的城市，对应的城市的天气信息
    - show_weather()
      参数：无
      作用：显示每次查询城市的天气信息
      返回值：无
    - history_data()
      参数：无
      作用：保存没有查询的信息
      返回值：无
    - help()
      作用：显示帮助信息

优化定时功能
    - 函数：run_function
    - 参数：定时间隔（单位秒），查询城市，类weatherfetch实例
    - 作用，在设置的间隔内不停的循环
    - 附加说明：
        1. 使用sched类实现定时功能；
        2. 调用sched类中scheduler函数、enter函数、runh函数
        3. enter函数第三个参数为需要循环的函数名，第四个参数是循环的函数的参数。

优化思想：
    - 解决上一版进入自动更新后，无法再次进入单次查询的问题。
    - 设置了定时参数auto_interval，该参数可以任意配置，为了便于观察，程序中时间的范围是1-12s。








