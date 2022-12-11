from backend_api import db
from datetime import datetime



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    instructions = db.Column(db.String(500), nullable=False)
    favorite = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.name}'
    
    def __init__(self, name, ingredients, instructions, favorite, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.favorite = favorite
        self.rating = rating



