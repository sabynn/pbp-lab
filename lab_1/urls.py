from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # TODO Add friends path using friend_list Views
]
