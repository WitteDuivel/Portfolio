from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("skills/", SkillsView.as_view(), name="skills"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("contact/", ContactView.as_view(), name="contact"),
]