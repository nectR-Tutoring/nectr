from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")


@given("Mike is on nectr home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url + "/")


@step("Mike scrolls down to links")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Mike should be redirected to "About" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    WebDriverWait(context.driver, 10).until(
        EC.title_contains('About nectR'))
