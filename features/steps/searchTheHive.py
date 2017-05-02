from behave import *
from django.contrib import auth
from django.test import Client
from django.urls import resolve
from hamcrest import has_entry, has_key, has_value, contains, has_property, is_, contains_string, starts_with, not_none
from hamcrest.core import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.factories import RegisteredUserFactory
from nectr.tutor.tests.factories import TutorFactory
from nectr.users.models import User

use_step_matcher("parse")


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
    u = User.objects.get(username=context.current_user.username)
    assert_that(u.first_name, contains_string(name), "User should match step name")
    u.set_password("password")
    assert c.login(username=u.username, password="password")


@given("{first_name} is a registered user")
def step_impl(context, first_name):
    """
    :type first_name: str
    :type context: behave.runner.Context
    """
    nectr_user = RegisteredUserFactory(first_name=first_name)
    lower_first_name = first_name.lower()
    assert_that(nectr_user.first_name, is_(first_name), "Has correct first name")
    assert_that(nectr_user.username, contains_string(lower_first_name), "Has Username containing first name")
    assert_that(nectr_user.email, starts_with(lower_first_name), "Has email containing first name")
    assert_that(nectr_user.password, is_(not_none()), "Has a password")
    assert_that(nectr_user.is_active, is_(True), "Should be an 'Active' user")

    context.current_user = nectr_user


@given("{name} is on search the hive page")
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url + "/search_the_hive/")


@when("{name} types {search_text} in search box")
def step_impl(context, name, search_text):
    """
    :type search_text: str
    :type name: str
    :type context: behave.runner.Context
    """
    search_field = context.driver.find_element_by_name('search_text')
    search_field.send_keys(search_text)


@step("clicks search the hive button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('search_button').click()


@then("he is directed to list of tutors page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("he can view preview of tutor dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    search_result_table = WebDriverWait(context.driver, 2).until(
        EC.presence_of_element_located((By.ID, "tutors_search_result_table"))
    )
    rows = search_result_table.find_elements_by_css_selector('td.tutor-result')



@step("he will see a view dashboard button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("there are 15 Math tutors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    TutorFactory.create_batch(size=15)


@step("he can view preview of tutor profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("he will see a view profile button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Billy clicks on search bar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('Billy enters "Math"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('Billy clicks "Submit" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("search results are loaded on search the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("10 tutor search results are displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('each search result contains "view tutor profile" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("remaining 5 tutors are diaplyed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("there are 5 C++ Programming tutors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('Billy enters "C++ Programming"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Billy clicks "more results" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("there are 5 C++ Programming tutors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('Billy enters "C++ Programming"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("5 tutor search results are displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("there are 5 C++ Programming tutors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('Billy enters "C++ Programming"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("there are 5 C++ Programming tutors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("there are 5 Cpp Programming tutors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('Billy enters "Cpp Programming"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
