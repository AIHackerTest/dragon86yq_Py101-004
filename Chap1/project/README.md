#### 天气查询程序

##### 功能
最简天气查询程序，运行在命令行界面，可实现以下功能：
- 输入城市名，返回该城市的天气数据；
- 输入help，可以显示帮助文档；
- 输入quit，可以退出程序的交互；
- 输入history，打印查询过的所有城市。

##### 函数说明
- load_data(): 实现.txt文件数据的读取
参数
1. filename：需要读取的文件名
return：
1. 字典数据

- help():输出帮助信息

- weather_inquired(): 存储历次输入的城市名和对应的天气
参数：
1. city：输入的城市名，
2. user_weathe:将历次输入的城市名和对应的天气存入字典
3. city_weather：load_data()返回的数据
return:
1. 历次输入的城市名和对应的天气

- show_info(): 出处历次存储的城市名和对应的天气
参数：
1. user_weathe:历次输入的城市名和对应的天气
