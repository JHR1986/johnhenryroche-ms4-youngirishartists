from django.test import TestCase


# Create your tests here.
def test_get_products(self):
    response = self.client.get('/products/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'products/products.html')


def test_get_products_detail(self):
    response = self.client.get('/products/2')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'products/product_detail.html')