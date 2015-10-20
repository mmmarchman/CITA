#!/usr/bin/python

import sys
import logging

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/html/CITA/Web/")

import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
import plotly.plotly as py

py.sign_in('mmmarchman', 'jqfkdptmgy')

application = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
	application.run()

