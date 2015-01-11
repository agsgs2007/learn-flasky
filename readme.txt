1、创建该文件夹learn-flasky
2、创建虚拟环境
virturalenv venv
从而创建了一个文件夹
3、打开管理员的cmd控制台，输入venv\Scripts\activate
从而激活了虚拟环境，这样python、pip等都使用的事venv\lib内的副本，不会对外部有任何影响
4、然后pip install flask安装flask库
5、打开pycharm，open learn-flasky文件夹，这为项目文件
6、激活pycharm的VCS系统，选择git
7、设计忽略文件，忽略.idea及venv

2015.1.11
1、安装上flask-script
2、重构代码，重点是生成Manager(app)
3、在命令行模式下输入：python hello.py runserver --host 0.0.0.0，在网段的其他的电脑都能登陆此服务器
4、手机上验证成功
		在手机浏览器输入192.168.0.104:5000，即显示
5、创建了base.html模板
6、根据base模板，创建了index,user,404页面
7、创建了form表单，使用了wtf快速表单技术
8、使用了flash技术，此时由于直接在代码中输入中文，出现了unicodeerror问题，最后使用了u''来解决
9、创建了数据库，使用sqlite3；
10、创建了命令行，使用了数据迁移