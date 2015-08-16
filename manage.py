import os
from flask.ext.script import Manager, Server
from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()