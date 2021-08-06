from django.urls import path
from . import views


# URL path for artists
urlpatterns = [
    path('', views.all_artists, name='artists')
]
