import factory
from django.template.defaultfilters import slugify
from factory import lazy_attribute, PostGenerationMethodCall
import faker

from nectr import users

faker_data = faker.Factory.create()  # separate to a factory boy Factory


class VisitorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    first_name = lazy_attribute(lambda o: faker_data.first_name())
    last_name = lazy_attribute(lambda o: faker_data.last_name())
    email = lazy_attribute(lambda o: faker_data.email())
    username = factory.Sequence(lambda n: "user_{0}".format(n))


class RegisteredUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    first_name = lazy_attribute(lambda o: faker_data.first_name())
    last_name = lazy_attribute(lambda o: faker_data.last_name())
    username = lazy_attribute(lambda a: slugify(a.first_name + '.' + a.last_name))
    email = lazy_attribute(
        lambda o: o.username + "@example.com")  # factory.lazy_attribute(lambda a: a.username + '@example.com')
    password = PostGenerationMethodCall('set_password', 'password')
