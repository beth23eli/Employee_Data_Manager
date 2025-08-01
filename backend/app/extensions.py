from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from flask_mail import Mail
from fpdf import FPDF
from datetime import datetime
from dateutil.relativedelta import relativedelta

db = SQLAlchemy()
faker = Faker()
mail = Mail()
previous_month = datetime.now() - relativedelta(months=1)

class PDF(FPDF):
    pass
pdf = PDF()