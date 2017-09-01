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
        for family_member in family_dict:

            #Name cannot be None
            self.assertIsNotNone(family_member['name'])
            self.assertIsNotNone(family_member['status'])

            #Name cannot be integer
            self.assertIsNot(type(family_member['name']),type(8))

    def test_lab2_family_member_shown_in_page(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')

        # Checking all family member is shown in page
        for family_member in family_dict:
            self.assertIn('<td class="status">' + family_member['status'] + '</td>', html_response)
            self.assertIn('<td class="name">' + family_member['name'] + '</td>', html_response)

    def test_lab2_have_button_next(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')
        self.assertIn('<button id="next_button" name="first_pop_button" class="btn btn-primary">Go to Lab 2 Addon</button>', html_response)