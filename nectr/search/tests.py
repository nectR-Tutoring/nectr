from django.test import TestCase


# Create your tests here.
class SearchTests(TestCase):
    def test_can_receive_a_POST(self):
        response = self.client.post('/search', data={'search_text': 'Computer Science'})
        self.assertIn('Computer Science', response.content.decode())
