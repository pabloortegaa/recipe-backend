import pytest
from backend_api.models import Recipe
from backend_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe(name='Jamon con melon', ingredients='- Jamon - Melon', instructions='Cortar el jamon y el melon en rodajas y ponerlo en una bandeja', favorite=False, rating=3)
    db.session.add(recipe)
    db.session.commit()
    with app.test_client() as testing_client:
        yield testing_client
    db.drop_all()

