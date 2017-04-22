from django.test import TestCase
from hamcrest import assert_that, has_property

from nectr.tutor.models import Tutor
from nectr.tutor.tests.factories import TutorFactory


class TutorModelTest(TestCase):
    pass
    # def test_saving_and_retrieving_tutors(self):
    #     first_tutor = TutorFactory()
    #     second_tutor = TutorFactory()
    #
    #     saved_tutors = Tutor.objects.all()
    #     self.assertEqual(saved_tutors.count(), 2)
    #
    #     assert_that(first_tutor, has_property('username'))
    #     assert_that(second_tutor, has_property('username'))
