from django.conf.urls import url
from hello_name import views
#url for app
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
