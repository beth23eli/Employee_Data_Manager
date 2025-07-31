from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from flask_mail import Mail
from fpdf import FPDF

db = SQLAlchemy()
faker = Faker()
mail = Mail()


class PDF(FPDF):
    pass
pdf = PDF()