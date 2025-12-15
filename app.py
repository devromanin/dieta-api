from flask import Flask
from database import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db.init_app(app)

