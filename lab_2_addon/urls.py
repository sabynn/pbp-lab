from django.conf.urls import url
from .views import index
#url for lab_2
#TODO Implement this
#Add Url that when accessing root url Lab 2, it will generate page index_lab2.html
urlpatterns = [
    url(r'^$', index, name='index'),
]
