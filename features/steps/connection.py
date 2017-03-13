from behave import *
from features.factories import VisitorFactory
from hamcrest import *

use_step_matcher("parse")


@given("I am a visitor")
def create_visitor(context):
    """
    :type context: behave.runner.Context
    """
    # context.visitor = VisitorFactory()
    pass


@when('I go to "{url}"')
def step_impl(context, url):
    """
    :param url: "/" homepage
    :type context: behave.runner.Context
    """
    context.response = context.browser.chrome.get(context.get_url(url))


@then('I should see the "Home Page"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('There should be a "Sign In" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('There should be a "Sign Up" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
