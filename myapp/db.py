import psycopg2
import click

from flask import current_app, g
from .settings import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD

from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD,
        )
    return g.db


def close_db():
    conn = g.pop('db', None)

    if conn is not None:
        conn.close()


def init_db():
    conn = get_db()
    cur = conn.cursor()

    with current_app.open_resource('schema.sql') as f:
        cur.execute(f.read().decode('utf8'))
    conn.commit()
    cur.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
