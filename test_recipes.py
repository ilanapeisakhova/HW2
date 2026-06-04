import pytest
from recipes import Ingredient, Recipe, ShoppingList

class TestIngredient:
    def test_create_ingredient(self):
        ingredient = Ingredient("Мука", 500.0, "г")
        assert ingredient.name == "Мука"
        assert ingredient.quantity == 500.0
        assert ingredient.unit == "г"
    
    def test_create_ingredient_positivequantity(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", -500, "г")
        with pytest.raises(ValueError):
            Ingredient("Мука", 0, "г")
    
    def test_str(self):
        ingredient = Ingredient("Мука", 500.0, "г")
        assert str(ingredient) == "Мука: 500.0 г"
    
    def test_eq(self):
        ingredient1 = Ingredient("Мука", 500, "г")
        ingredient2 = Ingredient("Мука", 1000, "г")
        ingredient3 = Ingredient("Подсолнечное масло", 500, "г")
        ingredient4 = Ingredient("Мука", 500, "кг")
        
        assert ingredient1 == ingredient2
        assert ingredient1 != ingredient3
        assert ingredient1 != ingredient4




class TestRecipe:
    def test_create_recipe(self):
        ingredient1 = Ingredient("Мука", 500, "г")
        ingredient2 = Ingredient("Яйца", 5, "шт")
        ingredients = [ingredient1, ingredient2]
        recipe = Recipe("Пирог", ingredients)
        
        assert recipe.title == "Пирог"
        assert recipe.ingredients[0].name == "Мука"
        assert recipe.ingredients[1].name == "Яйца"
        assert len(recipe.ingredients) == 2

    def test_add1(self):
        recipe = Recipe("Пирог", [Ingredient("Яйца", 5, "шт"), Ingredient("Молоко", 500, "г")])
        ingredient = Ingredient("Мука", 500, "г")
        recipe.add_ingredient(ingredient)
        
        assert len(recipe) == 3
        assert recipe.ingredients[2].name == "Мука"
        assert recipe.ingredients[2].quantity == 500
    
    def test_add2(self):
        ingredient1 = Ingredient("Мука", 500, "г")
        recipe = Recipe("Пирог", [ingredient1])
        ingredient2 = Ingredient("Мука", 100, "г")
        recipe.add_ingredient(ingredient2)
        
        assert len(recipe) == 1
        assert recipe.ingredients[0].quantity == 600
    
    def test_scale(self):
        ingredient = Ingredient("Мука", 500, "г")
        recipe = Recipe("Пирог", [ingredient])
        new_recipe = recipe.scale(3)
        
        assert recipe.ingredients[0].quantity == 500
        assert new_recipe.ingredients[0].quantity == 1500
        assert new_recipe.title == "Пирог"
    
    def test_len(self):
        ingredient1 = Ingredient("Мука", 500, "г")
        ingredient2 = Ingredient("Яйца", 5, "шт")
        recipe = Recipe("Пирог", [ingredient1, ingredient2])
        
        assert len(recipe) == 2




class TestShoppingList:
    def test_add_recipe(self):
        ingredient = Ingredient("Мука", 500, "г")
        recipe = Recipe("Пирог", [ingredient])
        lst = ShoppingList()
        lst.add_recipe(recipe, 3)
        
        assert len(lst._items) == 1
        assert lst._items[0][0].quantity == 1500
        assert lst._items[0][1] == "Пирог"
    
    def test_add_recipe_minus_portions(self):
        ingredient = Ingredient("Мука", 500, "г")
        recipe = Recipe("Пирог", [ingredient])
        lst = ShoppingList()
        
        with pytest.raises(ValueError):
            lst.add_recipe(recipe, -5)
        with pytest.raises(ValueError):
            lst.add_recipe(recipe, 0)
    
    def test_remove_recipe(self):
        ingredient = Ingredient("Мука", 500, "г")
        recipe1 = Recipe("Пирог", [ingredient])
        recipe2 = Recipe("Торт", [ingredient])
        lst = ShoppingList()
        
        lst.add_recipe(recipe1, 1)
        lst.add_recipe(recipe2, 1)
        assert len(lst._items) == 2
        
        lst.remove_recipe("Пирог")
        assert len(lst._items) == 1
        assert lst._items[0][1] == "Торт"
    
    def test_remove_recipe_not_exists(self):
        lst = ShoppingList()
        lst.remove_recipe("Абракадабра")
    
    def test_get_list1(self):
        ingredient1 = Ingredient("Мука", 500, "г")
        ingredient2 = Ingredient("Мука", 100, "г")
        recipe1 = Recipe("Пирог", [ingredient1])
        recipe2 = Recipe("Торт", [ingredient2])
        lst = ShoppingList()
        
        lst.add_recipe(recipe1, 1)
        lst.add_recipe(recipe2, 1)
        
        result = lst.get_list()
        assert len(result) == 1
        assert result[0].name == "Мука"
        assert result[0].quantity == 600
    
    def test_get_list2(self):
        ingredient1 = Ingredient("Яйца", 2, "шт")
        ingredient2 = Ingredient("Мука", 500, "г")
        ingredient3 = Ingredient("Масло", 100, "мл")
        recipe = Recipe("Пирог", [ingredient1, ingredient2, ingredient3])
        lst = ShoppingList()
        lst.add_recipe(recipe, 1)
        result = lst.get_list()
        names = [ing.name for ing in result]

        assert names == sorted(names)
    
    def test_add(self):
        ingredient1 = Ingredient("Мука", 500, "г")
        ingredient2 = Ingredient("Яйца", 2, "шт")
        recipe1 = Recipe("Пирог", [ingredient1])
        recipe2 = Recipe("Яичшица", [ingredient2])
        list1 = ShoppingList()
        list2 = ShoppingList()
        list1.add_recipe(recipe1, 1)
        list2.add_recipe(recipe2, 1)
        
        new = list1 + list2
        assert len(new._items) == 2
        
        # исходные списки не изменились
        assert len(list1._items) == 1
        assert len(list2._items) == 1