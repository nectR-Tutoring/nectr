from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from hamcrest import assert_that, contains_string

from nectr.search.models import Search
from nectr.search.views import search_page


class SearchTests(TestCase):
    def test_root_url_resolves_to_search_page_view(self):
        found = resolve('/search/')
        self.assertEqual(found.func, search_page)

    def test_search_page_returns_correct_title(self):
        request = HttpRequest()
        response = search_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        assert_that(html, contains_string('<title>Search Tutors'))
        self.assertTrue(html.strip().endswith('</html>'))

    def test_search_page_returns_correct_template(self):
        response = self.client.get('/search/')
        self.assertTemplateUsed(response, 'search.html')

    def test_can_receive_a_POST(self):
        response = self.client.post('/search/',
                                    data={'search_text': 'Computer Science'})
        self.assertIn('Computer Science', response.content.decode())
        self.assertTemplateUsed(response, 'search.html')

    def test_saving_and_retrieving_items(self):
        first_item = Search()
        first_item.search_text = 'The first (ever) search'
        first_item.save()

        second_item = Search()
        second_item.search_text = 'search the second'
        second_item.save()

        saved_items = Search.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.search_text, 'The first (ever) search')
        self.assertEqual(second_saved_item.search_text, 'search the second')

    def test_can_save_a_POST(self):
        response = self.client.post('/search/',
                                    data={'search_text': 'Computer Science'})
        self.assertEqual(Search.objects.count(), 1)

    def test_only_saves_items_when_necessary(self):
        self.client.get('/search/')
        self.assertEqual(Search.objects.count(), 0)
