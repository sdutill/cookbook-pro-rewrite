from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "public/home.html"


class RecipePageView(LoginRequiredMixin, TemplateView):
    template_name = "private/recipes.html"
    login_url = "login"
