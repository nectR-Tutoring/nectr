from behave import *
from selenium import webdriver
from hamcrest import assert_that, is_
import requests

use_step_matcher("re")


@given('The Server is Running on "Localhost"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.host = "localhost"


@step("On Port 8000")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.port = "8000"


@when("I visit http://localhost:8000")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = "http://" + context.host + ":" + context.port
    context.response = requests.get(url)


@then("I should get a 200 response")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    r = context.response
    assert_that(r.status_code, is_(200))
