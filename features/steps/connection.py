from behave import *
from django.test import Client
from django.conf import settings
from features.factories import VisitorFactory
from hamcrest import *

use_step_matcher("parse")


@given('I go to "{url}"')
def step_impl(context, url):
    """
    :param url: "/" homepage
    :type context: behave.runner.Context
    """
    pass


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


@step('There should be a "Sign Up" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
