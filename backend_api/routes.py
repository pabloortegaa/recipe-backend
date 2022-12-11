from flask import Flask, request
from backend_api import app, db
from backend_api.models import Recipe

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'], favorite=data['favorite'], rating=data['rating'])
    db.session.add(new_recipe)
    db.session.commit()
    return format_recipe(new_recipe), 201

@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi this is the backend skull'

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes= Recipe.query.order_by(Recipe.rating.desc()).all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    #recipe= Recipe.query.order_by(Recipe.ratings).all()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    data = request.get_json()
    recipe.name = data['name']
    recipe.ingredients = data['ingredients']
    recipe.instructions = data['instructions']
    recipe.favorite = data['favorite']
    recipe.rating = data['rating']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)


def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'favorite': recipe.favorite,
        'rating': recipe.rating,
        'date_created': recipe.date_created
    }