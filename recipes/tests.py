from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe, Ingredient, RecipeIngredients


class RecipeTestCase(TestCase):

    def setUp(self):
        """
        Setup test environment: Create a user, some ingredients, and a recipe.
        """
        # Create a custom user (since we're using AUTH_USER_MODEL)
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Sugar')
        self.ingredient2 = Ingredient.objects.create(name='Flour')

        # Create a recipe
        self.recipe = Recipe.objects.create(
            name='Pancake', created_by=self.user, instructions='Mix the ingredients and cook.'
        )

        # Add ingredients to the recipe
        RecipeIngredients.objects.create(
            recipe=self.recipe, ingredient=self.ingredient1, quantity=1, unit='cups'
        )
        RecipeIngredients.objects.create(
            recipe=self.recipe, ingredient=self.ingredient2, quantity=2, unit='cups'
        )

    def test_ingredient_creation(self):
        """Test if ingredients are created correctly."""
        self.assertEqual(self.ingredient1.name, 'Sugar')
        self.assertEqual(self.ingredient2.name, 'Flour')

    def test_recipe_creation(self):
        """Test if a recipe is created correctly with the right user and instructions."""
        self.assertEqual(self.recipe.name, 'Pancake')
        self.assertEqual(self.recipe.created_by.username, 'testuser')
        self.assertEqual(self.recipe.instructions, 'Mix the ingredients and cook.')

    def test_recipe_ingredients(self):
        """Test if the ingredients are correctly linked to the recipe."""
        # Updated to use recipeingredients_set
        recipe_ingredients = self.recipe.recipeingredients_set.all()
        self.assertEqual(recipe_ingredients.count(), 2)
        self.assertEqual(recipe_ingredients[0].ingredient.name, 'Sugar')
        self.assertEqual(recipe_ingredients[1].ingredient.name, 'Flour')

    def test_recipe_ingredient_quantity_and_unit(self):
        """Test if the quantity and unit for ingredients in the recipe are correct."""
        recipe_ingredient1 = self.recipe.recipeingredients_set.get(ingredient=self.ingredient1)
        recipe_ingredient2 = self.recipe.recipeingredients_set.get(ingredient=self.ingredient2)

        self.assertEqual(recipe_ingredient1.quantity, 1)
        self.assertEqual(recipe_ingredient1.unit, 'cups')

        self.assertEqual(recipe_ingredient2.quantity, 2)
        self.assertEqual(recipe_ingredient2.unit, 'cups')

    def test_recipe_ingredient_get_unit_display(self):
        """Test if the `get_unit_display` method works correctly for units."""
        recipe_ingredient = self.recipe.recipeingredients_set.get(ingredient=self.ingredient1)
        self.assertEqual(recipe_ingredient.get_unit_display(), 'Cups')

    def test_recipe_creation_timestamp(self):
        """Test if the created_at timestamp is automatically set."""
        self.assertIsNotNone(self.recipe.created_at)

    def test_recipe_str_method(self):
        """Test if the `__str__` method for the Recipe model works correctly."""
        self.assertEqual(str(self.recipe), 'Pancake')

    def test_ingredient_str_method(self):
        """Test if the `__str__` method for the Ingredient model works correctly."""
        self.assertEqual(str(self.ingredient1), 'Sugar')
        self.assertEqual(str(self.ingredient2), 'Flour')

    def test_recipe_ingredient_str_method(self):
        """Test if the `__str__` method for the RecipeIngredients model works correctly."""
        recipe_ingredient = self.recipe.recipeingredients_set.first()
        self.assertEqual(str(recipe_ingredient), '1.00 cups of Sugar')

    def test_user_association_in_recipe(self):
        """Test if the correct user is associated with a recipe."""
        self.assertEqual(self.recipe.created_by, self.user)
