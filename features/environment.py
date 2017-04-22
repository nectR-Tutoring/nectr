import os
import django
from django.core import management
from django.test import LiveServerTestCase
from django.test.runner import DiscoverRunner
from selenium import webdriver

# Even though DJANGO_SETTINGS_MODULE is set, this may still be
# necessary. Or it may be simple CYA insurance.
from splinter import Browser

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
    # setup_debug_on_error(context.config.userdata)

    # Boilerplay Manual Django Integration
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()


def before_feature(context, feature):
    if "browser-grid" in feature.tags:
        context.server_url = "http://django:8000"
        context.driver = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities={"browserName": "firefox", })
    if "browser" in feature.tags:
        context.browser = Browser()


def before_scenario(context, scenario):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()


def after_feature(context, feature):
    if 'browser-grid' in feature.tags:
        context.driver.quit()
        context.driver = None
    if 'browser' in feature.tags:
        context.browser.quit()
        context.browser = None


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
