from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'cooking_experience')

    cooking_experience = forms.ChoiceField(
        choices=CustomUser.COOKING_EXPERIENCE_CHOICES,
        required=True
    )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'cooking_experience')

    cooking_experience = forms.ChoiceField(
        choices=CustomUser.COOKING_EXPERIENCE_CHOICES,
        required=True
    )