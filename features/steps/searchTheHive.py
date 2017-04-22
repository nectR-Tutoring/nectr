from behave import *
from django.test import Client
from django.urls import reverse
from hamcrest import is_, contains_string, starts_with, not_none, contains_inanyorder
from hamcrest.core import assert_that
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from features.factories import VisitorFactory
from nectr.users.tests.factories import UserFactory

use_step_matcher("parse")


@given("{first_name} is a registered user")
def step_impl(context, first_name):
    """
    :type first_name: str
    :type context: behave.runner.Context
    """
    nectr_user = UserFactory(
        first_name=first_name,
        username="{0}.username".format(first_name),
        email="{0}@example.com".format(first_name),
    )

    assert_that(nectr_user.first_name, is_(first_name), "Has correct first name")
    assert_that(nectr_user.username, contains_string(first_name), "Has Username containing first name")
    assert_that(nectr_user.email, starts_with(first_name), "Has email containing first name")
    assert_that(nectr_user.password, is_(not_none()), "Has a password")
    assert_that(nectr_user.is_active, is_(True), "Should be an 'Active' user")

    context.current_user = nectr_user


@step("{name} is not signed into nectr")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    assert False


@given("{name} is signed into nectr")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """

    c = Client()
    assert_that(context.current_user.first_name, contains_string(name), "User should match step name")
    assert c.login(username=context.current_user.username, password="password")


@given("{name} is on search the hive page")
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url + reverse('search'))


@when("{name} types {search_text} in search box")
def step_impl(context, name, search_text):
    """
    :type search_text: str
    :type name: str
    :type context: behave.runner.Context
    """
    context.search_text = search_text
    search_field = context.driver.find_element_by_id('searchbar')
    search_field.send_keys(search_text)


@when("{name} types {search_text} in search box and presses ENTER")
def step_impl(context, name, search_text):
    """
    :type search_text: str
    :type name: str
    :type context: behave.runner.Context
    """
    search_field = context.driver.find_element_by_id('searchbar')
    search_field.send_keys(search_text, Keys.ENTER)


@step("{name} clicks search the hive button")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    search_button = context.driver.find_element_by_id('search_button')
    search_button.click()


@then("{name} is directed to list of tutors page")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Search"))
    # assert_that(context.driver.title, contains_string("Search"),
    #             "The current url is {0}.".format(
    #                 context.driver.current_url))
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Tutor"))


@step("he can view preview of tutor profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("The driver is currently on {0}".format(context.driver.current_url))
    table = context.driver.find_element_by_id('list_of_tutors')
    rows = table.find_elements_by_tag_name('tr')
    assert_that(
        any(row.text == context.search_text for row in rows),
        "Search Text did not Appear in Row. "
        "Contents were:\n{0}".format(table.text)
    )


@step("he will see a view profile button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    table = context.driver.find_element_by_id('list_of_tutors')
    buttons = table.find_elements_by_tag_name('button')
    assert_that(
        any(button.text == 'View Profile' for button in buttons),
        "View Profile button did not appear in row "
        "Contents were:\n{0}".format(table.text)
    )


@step('the search text "{search_text}" is in title')
def step_impl(context, search_text):
    """
    :type search_text: str
    :type context: behave.runner.Context
    """
    assert_that(context.driver.title, contains_string(search_text))


@given("{name} is on the home page")
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    context.visitor = VisitorFactory(first_name=name)
    context.driver.get(context.server_url + reverse('home'))
    assert_that(context.driver.title, contains_string("Home"))


@step('{name}\'s search "{search_text}" is in the title')
def step_impl(context, name, search_text):
    """
    :type name: str
    :type search_text: str
    :type context: behave.runner.Context
    """
    assert_that(context.driver.title, contains_string(search_text))


@when('{name} clicks "{button_name}"')
def step_impl(context, name, button_name):
    """
    :param name: str
    :type button_name: str
    :type context: behave.runner.Context
    """
    button = context.driver.find_element_by_name(button_name)
    button.click()
