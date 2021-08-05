from django.urls import path
from . import views


# URL pattern for about page.
urlpatterns = [
    path('', views.all_teams, name='teams')
]
