import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

# конфигурация
DATABASE = '/tmp/lms.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
app = Flask(__name__)
app.config.from_object(__name__)
import logging

# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть
# значений через переменную окружения
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'lms.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Соединяет с указанной базой данных."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Если ещё нет соединения с базой данных, открыть новое - для
    текущего контекста приложения
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    logging.info("Init DB")
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select * from users')
    entries = cur.fetchall()
    return "Hello, World!"


@app.route('/add_course', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into courses (name) values (?)',
               [request.form['name']])
    db.commit()

    flash('New entry was successfully posted')
    return ""


@app.route('/get_course', methods=['GET'])
def get_course():
    db = get_db()
    cur = db.execute('select * from courses where name == (?)',
                     [request.form['name']])
    db.commit()

    courses = cur.fetchall()
    flash('New entry was successfully posted')
    return courses[0]["name"]


if __name__ == '__main__':
    logging.basicConfig(level=4)
    # init_db()
    app.run()
