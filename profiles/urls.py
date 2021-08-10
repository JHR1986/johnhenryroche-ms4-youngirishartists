from django.urls import path
from . import views


# Create your tests here.
urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
]
