from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret")

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    FROM_EMAIL_ADDRESS = os.getenv("FROM_EMAIL_ADDRESS")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True