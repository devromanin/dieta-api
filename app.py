from flask import Flask
from flask_migrate import Migrate
from database import db
from dotenv import load_dotenv
from models.meal import Meal
from routes.meal_routes import meal_bp
import os



load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)



