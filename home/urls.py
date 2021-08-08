from django.urls import path
from . import views

# URL pattern for Home Page
urlpatterns = [
    path('', views.index, name='home')
]
