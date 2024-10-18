import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'oracle://STOCK:aa6e1f6c37@192.168.0.10:1521/desarrollo')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
