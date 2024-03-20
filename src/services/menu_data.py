import csv
from models.dish import Dish, Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str) -> set:
        dishes = []

        with open(source_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                dish = Dish(dish_name, price)

                if dish not in dishes:
                    dishes.append(dish)

                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name),
                    recipe_amount,
                )

        return dishes
