from behave import *
from django.test import Client

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
    client = Client()
    response = client.get('/')

    assert_that(response.content, contains_string("Home"))


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


@step('There should be a "signUp.feature" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
