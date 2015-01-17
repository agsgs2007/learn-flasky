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


2015.1.17
1、实践了第七章，将hello.py分解成几个文件，其中涉及到几个技术：
	1）模块的导入；
	2）__init__文件比较重要
	3）单元测试技术
	4）再次使用了manage和shell，这里有个细节
			由于采取了运行时生成app技术，不是直接运行启动的，所以一开始不知道app从哪里生成，但是实际上在manage.py中app一开始就由create_app产生，所以在命令行模式下是能使用这个实例的。
	5）数据迁移
			今天数据迁移并不成功，网页运行时，提交数据时提示没有这个表，说明数据库里面并没有这个表，所以需要手动生成表，经过研究，需要使用shell。
			从第4点看出，使用shell时，app能生成，所以可以在app_context下工作，步骤如下：
			>>>python manage.py shell
			>>>app
			>>>from app import db
			>>>db.create_all() #此步创建了数据库和表
			>>>from app.models import User,Role
			>>>User.query.all()  #此步能运行说明数据表已经创建成功
			
			然后再次运行网站python manage.py runserver
			在表单中输入数据提交，这次能够正常执行