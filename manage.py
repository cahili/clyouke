# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:44:02
# @Last Modified by:   Administrator
# @Last Modified time: 2016-09-05 22:46:45
import os
from app import create_app, db
from app.models import Jishuqu, Dagaier
from flask_script import Manager, Shell

app = create_app(os.getenv('CL_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Jishuqu=Jishuqu, Dagaier=Dagaier)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
