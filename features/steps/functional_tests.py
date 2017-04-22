from behave import *
from selenium import webdriver
from hamcrest import assert_that, is_, close_to, contains_string, isnone, not_none
import requests

use_step_matcher("parse")


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


@then("I should get a good response")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for links in context.links:
        value = links.get_attribute("href")
        r = requests.get(value)
        assert_that("Should get a good response on: {0}".format(r.text),
                    r.status_code, is_(close_to(300, 100)))


@given("I am on '{page}' with '{title}'")
def step_impl(context, page, title):
    """
    :type title: str
    :type page: str
    :type context: behave.runner.Context
    """
    driver = context.driver
    driver.get(context.server_url + page)
    assert_that(driver.title, contains_string(title))
    context.page = driver


@when("I request each '{html_element}'")
def step_impl(context, html_element):
    """
    :param html_element: 
    :type context: behave.runner.Context
    """
    elements = context.page.find_elements_by_xpath("//a[@{0}]".format(html_element))
    assert_that(elements, is_(not_none()))
    context.links = elements
