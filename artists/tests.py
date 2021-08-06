from django.test import TestCase


# Test Run for Artists View.
class TestViews(TestCase):

    def test_get_artists(self):
        response = self.client.get('/artists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artists/artists.html')
