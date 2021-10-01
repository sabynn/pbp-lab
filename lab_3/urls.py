from django.urls import path
from .views import index, add_friend

urlpatterns = [
    path('', index),
    path('add', add_friend),
]