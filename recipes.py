class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property.getter
    def quantity(self):
        return self._quantity
    
    @property.setter
    def quantity(self, number: float):
        if number <= 0:
            raise ValurError("Количество должно быть положительным")
        self._quantity = number

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.quantity == other.quantity