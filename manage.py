__author__ = 'zhangxun'
#coding:utf-8

import os
from app import create_app, db
from app.models import User,Role
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.script import Shell

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate=Migrate(app,db)

#增加命令行指令，初始化数据库，创建数据库模型，创建迁移仓库
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """run the unit tests 下面第二行代码寻找当前目录下的tests目录"""
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
#    app.run(debug=True)
    manager.run()