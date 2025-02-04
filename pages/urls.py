from django.urls import path

from .views import HomePageView, RecipePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("recipes/", RecipePageView.as_view(), name="recipes"),
]
