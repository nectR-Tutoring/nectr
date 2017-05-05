from behave import *
from django.test import Client
from django.conf import settings
from features.factories import VisitorFactory
from hamcrest import *

use_step_matcher("parse")


@when('I go to "{url}"')
def step_impl(context, url):
    """
    :param url: "/" homepage
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url+url)
    assert_that(context.driver.current_url, is_(context.server_url+url))


@then('I should see a page with title "{title}"')
def step_impl(context, title):
    """
    :param title: 
    :type context: behave.runner.Context
    """
    assert_that(context.driver.title, contains_string(title),
                "Page title contains the word home")


@then('There should be a "{text}" link with name "{name}"')
def step_impl(context, text, name):
    """
    :type text: str
    :type name: str
    :type context: behave.runner.Context
    """
    html_element = context.driver.find_element_by_name(name)
    assert_that(html_element.text, contains_string(text),
                "Element has correct text")


@when('I press the "{name}"')
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_name(name).click()


@then('There should be a "SIGN UP" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('sign-up-link')


@then('There should be a "LOG IN" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('log-in-link')
