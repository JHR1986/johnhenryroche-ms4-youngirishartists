from django.test import TestCase


# Create test for Home Page
class TestViews(TestCase):

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
