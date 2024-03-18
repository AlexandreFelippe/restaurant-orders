from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("massa de lasanha")
    ingredient3 = Ingredient("queijo mussarela")

    assert ingredient1.name == "queijo mussarela"

    assert ingredient1.name == ingredient3.name
    assert ingredient1.name != ingredient2.name

    assert ingredient1 != ingredient2
    assert ingredient1 == ingredient3

    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert hash(ingredient1) == hash(ingredient3)
    assert hash(ingredient1) != hash(ingredient2)
    assert ingredient2.restrictions == {
        Restriction.LACTOSE, Restriction.GLUTEN
        }
