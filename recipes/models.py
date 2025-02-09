from django.db import models
from django.conf import settings


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # Use CustomUser here
    created_at = models.DateTimeField(auto_now_add=True)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredients')

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    """this is the through table (also known as junction table brigde table) this assocaites a recipe with
    an ingredient also stores the quantity and unit of measurement of the ingredient"""

    UNIT_CHOICES = [  # add more unit choices here as needed
        ('cups', 'Cups'),
        ('tablespoons', 'Tablespoons'),
        ('teaspoons', 'Teaspoons'),
        ('grams', 'Grams'),
        ('kilograms', 'Kilograms'),
        ('liters', 'Liters'),
        ('milliliters', 'Milliliters'),
        ('oz', 'Ounces'),
        ('lbs', 'Pounds'),
        ('mg', 'Milligrams'),
        ('g', 'Grams'),
        ('pinch', 'Pinch'),
        ('dash', 'Dash'),
        ('cloves', 'Cloves'),
        ('whole', 'Whole'),
        ('slices', 'Slices'),
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name}"
