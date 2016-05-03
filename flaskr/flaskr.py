# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration - usually keep this in a separate file and load from it with app.config.from_object() which loads all UPPERCASE variables in the config file
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create the application
app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR SETTINGS', silent = True) # sets to check for a config file called FLASKR SETTINGS, and not complain if no such file exists

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()

from contextlib import closing

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
