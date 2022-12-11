
from backend_api.models import Recipe
from backend_api import db, app
import pytest

def test_create_recipe(): 
    recipe = Recipe(name='Jamon con melon', ingredients='- Jamon - Melon', instructions='Cortar el jamon y el melon en rodajas y ponerlo en una bandeja', favorite=False, rating=3)
    assert recipe.name == 'Jamon con melon'
    assert recipe.ingredients == '- Jamon - Melon'
    assert recipe.instructions == 'Cortar el jamon y el melon en rodajas y ponerlo en una bandeja'
    assert recipe.favorite == False
    assert recipe.rating == 3


