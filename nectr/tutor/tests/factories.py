import factory

from nectr.users.tests.factories import UserFactory


class TutorFactory(factory.Factory):
    user = factory.SubFactory(UserFactory)
    class Meta:
        model = 'tutor.Tutor'
