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
    context.driver.get(context.server_url+url)
    assert_that(context.driver.current_url, is_(context.server_url+url))


@then('I should see the "Home Page"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.driver.title, contains_string("Home"), "Page title contains the word home")


@step('There should be a "Sign In" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Get sign in element')


@step('There should be a "Sign Up" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Sign Up Link')
