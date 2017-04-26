import factory


class SearchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'search.Search'

    search_text = 'Search Text'

