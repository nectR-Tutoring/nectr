from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve

from nectr.search.views import search_page


class SearchTests(TestCase):
    def test_root_url_resolves_to_search_page_view(self):
        found = resolve('/search/')
        self.assertEqual(found.func, search_page)

    def test_search_page_returns_correct_title(self):
        request = HttpRequest()
        response = search_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Search Tutors</title>', html)
        self.assertTrue(html.endswith('</html>'))
    # def test_uses_search_template(self):
    #     response = self.client.get('/search/')
    #     self.assertTemplateUsed(response, 'search.html')

    # def test_can_receive_a_POST(self):
    #     response = self.client.post('search/', data={'search_text': 'Computer Science'})
    #     self.assertIn('Computer Science', response.content.decode())
