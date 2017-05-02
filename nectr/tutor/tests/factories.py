import factory

from nectr.users.tests.factories import UserFactory


class TutorFactory(factory.django.DjangoModelFactory):
    base_user = factory.SubFactory(UserFactory)
    votes

    class Meta:
        model = 'tutor.Tutor'
        django_get_or_create = ('base_user', )
