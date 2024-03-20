import csv
from models.dish import Dish, Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.ingredients = set()
        self.load_menu_data()

    def load_menu_data(self):
        with open(self.source_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                dish = self._get_or_create_dish(dish_name, price)
                ingredient = self._get_or_create_ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, recipe_amount)

    def _get_or_create_dish(self, name: str, price: float) -> Dish:
        dish = next(
            (plate for plate in self.dishes if plate.name == name),
            None)
        if dish is None:
            dish = Dish(name, price)
            self.dishes.add(dish)
        return dish

    def _get_or_create_ingredient(self, name: str) -> Ingredient:
        ingredient = next(
            (ing for ing in self.ingredients if ing.name == name),
            None)
        if ingredient is None:
            ingredient = Ingredient(name)
            self.ingredients.add(ingredient)
        return ingredient
