from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'

    COOKING_EXPERIENCE_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    cooking_experience = models.CharField(
        max_length=20,
        choices=COOKING_EXPERIENCE_CHOICES,
        default=BEGINNER,  # Set default to Beginner
    )

    def __str__(self):
        return self.username + ' (' + self.cooking_experience + ')'