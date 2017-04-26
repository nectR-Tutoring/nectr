from django.test import TestCase
from hamcrest import assert_that, is_

from nectr.search.tests.factories import SearchFactory


class TestSearchFactory(TestCase):
    def test_default_search(self):
        search = SearchFactory()
        assert_that(search.search_text, is_('Search Text'))

    def test_given_a_search_text(self):
        text = 'This is a Test'
        search = SearchFactory(search_text=text)
        assert_that(search.search_text, is_(text))
