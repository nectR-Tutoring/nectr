import factory


class TutorFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user-{0}'.format(n))

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)
