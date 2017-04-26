from django.test import TestCase
from hamcrest import assert_that, has_property, is_

from nectr.search.tests.factories import SearchFactory

#TODO::
class TestSearchTheHive(TestCase):
    def test_get_tutors_given_search_text(self):
        request = SearchFactory(search_text='Math')
        assert_that(request, has_property('search_text'))
        assert_that(request.search_text, is_('Math'))

        response = self.client.get('/search/tutors/', data={
            'search_text': request.search_text
        })
        self.assertEqual(response.status_code, 200)
