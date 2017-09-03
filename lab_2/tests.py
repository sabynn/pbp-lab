from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, landing_page_content, mhs_name
from django.http import HttpRequest


# Create your tests here.

class Lab2UnitTest(TestCase):

    def test_lab_2_url_is_exist(self):
        response = Client().get('/lab-2/')
        self.assertEqual(response.status_code,200)

    def test_root_url_now_is_using_index_page_from_lab_2(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_lab2_using_index_func(self):
        found = resolve('/lab-2/')
        self.assertEqual(found.func, index)

    def test_landing_page_content_is_written(self):
        #Content cannot be null
        self.assertIsNotNone(landing_page_content)

        #Content is filled with 30 characters at least
        self.assertTrue(len(landing_page_content) >= 30)

    def test_landing_page_is_completed(self):
        def test_index_contains_age(self):
            request = HttpRequest()
            response = index(request)
            html_response = response.content.decode('utf8')
            self.assertIn(html_response, '<p class="status">Hello, this is '+ mhs_name +'. '+ landing_page_content +' Check my <a id="href_bio">Biography</a>.</p>')
