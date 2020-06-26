import psycopg2
from flask import current_app, g
from current_app.config import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD


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
    db = g.pop('db', None)

    if db is not None:
        db.close()
