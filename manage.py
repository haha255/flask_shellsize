#!/usr/bin/env python3
import os
from app import create_app, db
from app.models import Pic_Table, Fanshell_data
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Pic_Table=Pic_Table, Fanshell_data=Fanshell_data)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
