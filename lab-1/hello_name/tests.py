from django.test import TestCase
from django.test import Client
from django.urls import resolve
from hello_name.views import index, mhs_name
from django.http import HttpRequest


# Create your tests here.

class HelloNameUnitTest(TestCase):
    def test_hello_name_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code,200)

    def test_using_index_func(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_name_is_changed(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')
        self.assertIn('<title>'+mhs_name+'</title>', html_response)
        self.assertIn('<h1>Hello My Name is ' + mhs_name + '</h1>', html_response)
        self.assertEqual(len(mhs_name),0)
