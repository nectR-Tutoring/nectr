import factory

from nectr.courses.factories import CoursesFactory
from nectr.users.tests.factories import UserFactory


class TutorFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    courses = factory.SubFactory(CoursesFactory)

    class Meta:
        model = 'tutor.Tutor'
        django_get_or_create = ('user', )
