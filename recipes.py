class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, number: float):
        if number <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = number

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title
        self.ingredients = ingredients.copy()

    def add_ingredient(self, ingredient: Ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)):
            return ratio > 0
        return False

    def scale(self, ratio: float):
        if self.is_valid_ratio(ratio):
            new = []
            for i in self.ingredients:
                new_ing = Ingredient(i.name, i.quantity * ratio, i.unit)
                new.append(new_ing)
            return Recipe(self.title, new)
        return Recipe(self.title, [])

    def __len__(self)-> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        result = f"Рецепт: {self.title}\nИнгредиенты:\n"
        for i in self.ingredients:
            result += f" - {i}\n"
        return result