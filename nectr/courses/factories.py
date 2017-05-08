import factory


class CoursesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'courses.Courses'
        django_get_or_create = ('course_name',)

    course_name = "Test Course"
