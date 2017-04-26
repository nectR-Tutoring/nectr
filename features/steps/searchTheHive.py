from behave import *
from django.contrib import auth
from django.test import Client
from django.urls import resolve
from hamcrest import has_entry, has_key, has_value, contains, has_property, is_, contains_string, starts_with, not_none
from hamcrest.core import assert_that
from selenium import webdriver

from features.factories import RegisteredUserFactory
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
    RegisteredUserFactory(first_name=name)
    c = Client()
    u = User.objects.get(first_name__exact=name)
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
    print (context.browser.current_url)
    search_field = context.browser.find_by_id('search_box')
    search_field.send_keys(search_text)



@step("clicks search the hive button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    search_button = context.browser.find_by_id('search')
    search_button.click()
    context.browser.save_screenshot('ClickSearchTheHive.png')


@then("he is directed to list of tutors page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("he can view preview of tutor profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("he will see a view profile button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False
