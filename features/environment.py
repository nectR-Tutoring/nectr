import os
import django
from django.core import management
from django.test import LiveServerTestCase
from django.test.runner import DiscoverRunner
from selenium import webdriver

# Even though DJANGO_SETTINGS_MODULE is set, this may still be
# necessary. Or it may be simple CYA insurance.
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test"
django.setup()

# -- FILE: features/environment.py
# USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)
# https://pythonhosted.org/behave/tutorial.html#debug-on-error-in-case-of-step-failures
BEHAVE_DEBUG_ON_ERROR = False


# https://pythonhosted.org/behave/tutorial.html#debug-on-error-in-case-of-step-failures
def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)

    # Boilerplay Manual Django Integration
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()

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


def before_feature(context, feature):
    if "browser-grid" in feature.tags:
        context.server_url = "http://django:8000"
        context.driver = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities={"browserName": "firefox", })
        context.driver.implicitly_wait(90)


def before_scenario(context, scenario):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()

    # Reset the database before each scenario
    # This means we can create, delete and edit objects within an
    # individual scenerio without these changes affecting our
    # other scenarios
    # management.call_command('flush', verbosity=0, interactive=False)

    # At this stage we can (optionally) mock additional data to setup in the database.
    # For example, if we know that all of our tests require a 'SiteConfig' object,
    # we could create it here.


def after_feature(context, feature):
    if 'browser-grid' in feature.tags:
        context.driver.quit()
        context.driver = None


def after_scenario(context, scenario):
    context.test_case.tearDownClass()
    del context.test_case


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
