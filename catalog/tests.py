from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import UserFavorite,Product,Category

# Create your tests here.

class PageTestCase(TestCase):
    
    """class PageTestCase"""
    # def test_base_page(self):
    #     """test_base_page"""
    #     response = self.client.get(reverse('catalog:base'))
    #     self.assertEqual(response.status_code, 200)

    def test_choosen_product_page(self):
        """test_choosen_product_page"""
        response = self.client.get(reverse('choosen_product',args=(self.product_id,)))
        query = ["steak haché"]
        self.assertEqual(response.status_code, 200)
    
    def test_favorits_page(self):
        """test_favorits_page"""
        response = self.client.get(reverse('favorits'))
        self.assertEqual(response.status_code, 302)

    def test_index_page(self):
        """test_index_page"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_search_result_page(self):
        """test_search_result_page"""
        response = self.client.get(reverse('search_result'))
        self.assertEqual(response.status_code, 200)
