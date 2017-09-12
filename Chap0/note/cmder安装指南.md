- Cmder下载地址：[Cmder](https://github.com/cmderdev/cmder/releases/)

- Cmder安装和配置：
    - 直接解压文件夹，运行Cmder.exe

    - 将Cmder添加到环境变量：把Cmder.exe存放的目录添加到系统环境变量，之后可以在Win+r输入Cmder就可以运行软件
        - 两种方法添加环境变量：
            1. 右键我的电脑属性 -> 左侧高级系统设置 -> 环境变量 -> 系统变量 -> 新建 -> 变量名：Path -> 变量值Cmder所在路径

    - 添加至右键：
        以管理员模式运行cmd，进入Cmder目录，输入 Cmder.exe /REIGSTER ALL

    - 解决乱码问题，并配置颜色：
        -将下列四行语句添加到Cmder目录下面-> config -> user-aliases.cmd文件中
        ```
        l=ls --show-control-chars  --color
        la=ls -aF --show-control-chars --color
        ll=ls -alF --show-control-chars --color
        ls=ls --show-control-chars -F --color
        ```
    - Cmder Ls目录中文显示编码的问题：
        在Cmder界面最下面右键点击settings -> Startup -> Environment 在右面空白框中填入：set LANG=zh_CN.UTF8

    - 中文文字乱码重叠的问题：
        在Cmder界面最下面右键点击settings -> Main ->去掉Monospace前面的勾

    - 关闭更新：
        在Cmder界面最下面右键点击settings -> Main -> Update 去掉Startup前面的勾

    - 将cmd中lamda修改为$
        修改安装包目录vendor下面的clink.lua文件，修改后如下
        ```
        if env == nil then
        lambda = "$"
        else
        lambda = "("..env..") $"
        ```
- cmd环境配置
     将环境变量Path设置为：%SystemRoot%/System32;%SystemRoot%

- 参考：[使用Cmder的几个问题](http://www.cnblogs.com/murphyzhao/p/6823627.html)
