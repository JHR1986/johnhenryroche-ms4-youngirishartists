from django.test import TestCase


# Create your tests here.
def test_get_bag(self):
    response = self.client.get('/bag/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'bag/bag.html')