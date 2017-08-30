from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, family_dict
from django.http import HttpRequest


# Create your tests here.

class Lab2UnitTest(TestCase):

    def test_lab_2_url_is_exist(self):
        response = Client().get('/lab-2/')
        self.assertEqual(response.status_code,200)

    def test_lab2_using_index_func(self):
        found = resolve('/lab-2/')
        self.assertEqual(found.func, index)

    def test_lab2_family_dict(self):
        #Check whether family_dict is not None Object
        self.assertIsNotNone(family_dict)

        #Checking all element in family member
        for family_member, name in family_dict.items():

            #Name cannot be None
            self.assertIsNotNone(name)

            #Name cannot be integer
            self.assertIsNot(type(name),type(8))

    def test_lab2_family_member_shown_in_page(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')

        # Checking all family member is shown in page
        for family_member, name in family_dict.items():
            self.assertIn('<td class="status">' + family_member + '</td>', html_response)
            self.assertIn('<td class="name">' + name + '</td>', html_response)

