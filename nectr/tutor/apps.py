from django.apps import AppConfig


class TutorConfig(AppConfig):
    name = 'nectr.tutor'
    verbose_name = "Tutors"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
