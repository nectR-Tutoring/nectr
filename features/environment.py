import os
import django
from django.core import management
from selenium import webdriver

# Even though DJANGO_SETTINGS_MODULE is set, this may still be
# necessary. Or it may be simple CYA insurance.
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test"
django.setup()


def before_all(context):
    context.server_url = "http://localhost:8000/"
    context.driver = webdriver.Remote(
        command_executor='http://hub:4444/wd/hub',
        desired_capabilities={
            "browserName": "firefox",
            "javascriptEnabled": True, })

    # ### Take a TestRunner hostage.
    # # from django.test.simple import DjangoTestSuiteRunner
    # # from django.test.runner import DiscoverRunner
    # # We'll use thise later to frog-march Django through the motions
    # # of setting up and tearing down the test environment, including
    # # test databases.
    # from django.conf import settings
    # from django.test.utils import get_runner
    # TestRunner = get_runner(settings)
    # context.test_runner = TestRunner()
    #
    # ## If you use South for migrations, uncomment this to monkeypatch
    # ## syncdb to get migrations to run.
    # # from south.management.commands import patch_for_test_db_setup
    # # patch_for_test_db_setup()
    #
    # ### Set up the WSGI intercept "port".
    # import wsgi_intercept
    # from django.core.handlers.wsgi import WSGIHandler
    # host = context.host = 'localhost'
    # port = context.port = getattr(settings, 'TESTING_MECHANIZE_INTERCEPT_PORT', 17681)
    # # NOTE: Nothing is actually listening on this port. wsgi_intercept
    # # monkeypatches the networking internals to use a fake socket when
    # # connecting to this port.
    # wsgi_intercept.add_wsgi_intercept(host, port, WSGIHandler)
    #
    # def browser_url(url):
    #     """Create a URL for the virtual WSGI server.
    #
    #     e.g context.browser_url('/'), context.browser_url(reverse('my_view'))
    #     """
    #     return urlparse.urljoin('http://%s:%d/' % (host, port), url)
    #
    # context.browser_url = browser_url
    #
    # ### BeautifulSoup is handy to have nearby. (Substitute lxml or html5lib as you see fit)
    # from BeautifulSoup import BeautifulSoup
    # def parse_soup():
    #     """Use BeautifulSoup to parse the current response and return the DOM tree.
    #     """
    #     r = context.browser.response()
    #     html = r.read()
    #     r.seek(0)
    #     return BeautifulSoup(html)
    #
    # context.parse_soup = parse_soup


def before_scenario(context, scenario):
    # Reset the database before each scenario
    # This means we can create, delete and edit objects within an
    # individual scenerio without these changes affecting our
    # other scenarios
    management.call_command('flush', verbosity=0, interactive=False)

    # At this stage we can (optionally) mock additional data to setup in the database.
    # For example, if we know that all of our tests require a 'SiteConfig' object,
    # we could create it here.


def after_all(context):
    context.driver.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass
