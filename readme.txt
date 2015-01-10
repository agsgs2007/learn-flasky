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