import factory

from nectr.users.tests.factories import UserFactory


class TutorFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = 'tutor.Tutor'
        django_get_or_create = ('user', )
