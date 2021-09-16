from django.urls import path
from .views import index, friend_list

urlpatterns = [
    path('', index, name='index'),
    path('friends', friend_list)
]
