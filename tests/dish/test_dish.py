from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    carbonara = Dish("Spaghetti Carbonara", 25.99)
    caccio_pepe = Dish("Spaghetti Caccio e Pepe", 25.99)
    caccio_pepe_2 = Dish("Spaghetti Caccio e Pepe", 25.99)

    carbonara.add_ingredient_dependency(Ingredient("massa de ravioli"), 5)
    carbonara.add_ingredient_dependency(Ingredient("ovo"), 8)

    assert carbonara.name == "Spaghetti Carbonara"
    assert carbonara.get_ingredients() == {
        Ingredient("massa de ravioli"),
        Ingredient("ovo"),
        }
    assert carbonara.__eq__(caccio_pepe) is False
    assert caccio_pepe.__eq__(caccio_pepe_2) is True
    assert repr(carbonara) == "Dish('Spaghetti Carbonara', R$25.99)"
    assert hash(carbonara) != hash(caccio_pepe)
    assert hash(caccio_pepe) == hash(caccio_pepe_2)

    assert carbonara.get_restrictions() == {
        Restriction.LACTOSE, Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED,
        }
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("caccio_pepe", "erro")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("carbonara", 0)
