import os

DEBUG = False
TESTING = False

SECRET_KEY = os.environ.get('SECRET_KEY')

DB_NAME = os.environ.get('DB_NAME')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
# DATABASE_URI = os.environ.get('DATABASE_URI')
