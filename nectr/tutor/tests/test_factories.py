from django.test import TestCase
from hamcrest import assert_that, has_properties, has_property

from nectr.tutor.tests.factories import TutorFactory


class TestTutorFactory(TestCase):

    def test_default_tutor_creation(self):
        tutor = TutorFactory()
        assert_that(tutor.base_user, has_property('username'))
        assert_that(tutor.base_user, has_property('first_name'))
        assert_that(tutor.base_user, has_property('last_name'))
        assert_that(tutor.base_user, has_property('email'))
