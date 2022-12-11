from backend_api import app
import pytest

def test_get_recipe(testing_client):
    response = testing_client.get('/recipes')
    assert response.status_code == 200


def test_dummy_wrong_route(): 

    with app.test_client() as client:
        response = client.get('/wrong_route')
        assert response.status_code == 404

def test_create_recipe(testing_client):
    response = testing_client.post('/recipes', json={'name': 'Jamon con melon', 'ingredients': '- Jamon - Melon', 'instructions': 'Cortar el jamon y el melon en rodajas y ponerlo en una bandeja', 'favorite': False, 'rating': 3})
    assert response.status_code == 201
