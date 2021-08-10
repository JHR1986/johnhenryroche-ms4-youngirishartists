from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):

    def test_get_profile_page(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
