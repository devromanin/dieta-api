from sqlalchemy import Nullable
from database import db
from datetime import datetime

__tablename__ = "meals"

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow nullable=False)
    description = db.Column(db.String(80), nullable=True)
    within_diet = db.Column(db.Boolean, nullable=False)


