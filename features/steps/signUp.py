from behave import *
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from nectr.users.models import User
from nectr.users.tests.factories import UserFactory

use_step_matcher("parse")


@given("{name} is not yet registered")
def step_impl(context, name):
    """
    :param name: name of user
    :type context: behave.runner.Context
    """
    UserFactory(username=name)
    assert_that(User.objects.all(), )



@given("Charlie is on the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("Charlie clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('is asked "{text}"')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("he says no")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Mike is on the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("mike clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("he says yes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then('he is redirected to the "sign up form"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Enoc is on the seacrch the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("enoc clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then('is redirected to the "sign up" form')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("brandon is on the about nectr page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("brandon clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("juan is on the how it works page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("juan clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Spongebob is on home page of nectr")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url + "/")


@step("Spongebob does not have nectR account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Spongebob clicks menu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_name("menu").click()


@step('Spongebob clicks "Sign Up" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('sign-up-link').click()


@step('title of the page is "Signup"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Signup"))
    current_page_title = context.driver.title
    assert_that(current_page_title, contains_string("Signup"))


@step('page contains an h1 whos text is "Sign up"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_tag_name('h1')


@when("Spongebob clicks on username text field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('id_username').click()


@step('Spongebob enters username "{some_text}"')
def step_impl(context, some_text):
    """
    :type some_text: str
    :type context: behave.runner.Context
    """
    element = context.driver.find_element_by_id("id_username")
    element.send_keys(some_text)



@step("Spongebob clicks on E-mail text field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('id_email').click()


@step("Spongebob clicks on password text field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Spongbob enters "CrabbyPatty2"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False




@step("Spongbob leaves this text field blank")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False






@step('title of the page is "Verify Your E-mail Address"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('page contains an h1 whos text is "Verify Your E-mail Address"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Spongebob checks his email "ayouf@farmingdale.edu"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Spongebob opens "confirm account" email')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Spongebob clicks account confirmation link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Spongebob enters "ayouf@farmingdale.edu"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False




@step("Spongebob clicks on Repeat Password field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False




@then('Spongebob gets "please fill out this field" alert in Password field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Spongebob cicks on Password field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False
