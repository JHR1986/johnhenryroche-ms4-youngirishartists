from django.test import TestCase


# Create your tests here.

class TestViews(TestCase):

    def test_get_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')