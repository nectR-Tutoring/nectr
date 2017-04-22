from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'nectr.search'
    verbose_name = "Search"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

