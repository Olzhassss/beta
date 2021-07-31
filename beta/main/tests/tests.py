from django.test import TestCase, SimpleTestCase
from main.models import Profile
from main.views import index, apply, reviewApplication
from django.urls import reverse, resolve

# Create your tests here.
class ProfileTestCase(TestCase):
    assert 1==1

from django.test import Client

class UrlTestCase(SimpleTestCase):
    # c = Client()
    
    def wrapper_test_url_resolves(self, url_name, view, class_based = False, *kwargs):
        expected_view = resolve(reverse(url_name, *kwargs)).func
        expected_view = expected_view.view_class if class_based else expected_view
        self.assertEquals(expected_view, view)
        # response = self.c.get('/apply')
        # assert response.code == '200'

    def test_application(self):
        self.wrapper_test_url_resolves('main:application', apply, False)

    def test_appBrowse(self):
        self.wrapper_test_url_resolves('main:appBrowse', apply, False, app_id='1')