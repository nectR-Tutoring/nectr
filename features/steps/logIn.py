from behave import *
from hamcrest import assert_that, has_entries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.factories import VisitorFactory
from nectr.users.models import User
from nectr.users.tests.factories import UserFactory

use_step_matcher("parse")


@given("{name} is not registered to nectr")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    VisitorFactory(first_name=name)


@given("{name} is registered to nectr")
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    UserFactory(username=name, password="password")


@given("{name} is on nectr site")
def step_impl(context, name):
    """
    :param name: str ID of User using Name
    :type context: behave.runner.Context
    """
    br = context.driver
    br.get(context.server_url)


@when("{name} clicks on login button")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """

    menu = context.wait.until(EC.element_to_be_clickable((By.NAME, "menu")))
    menu.click()

    context.driver.find_element_by_name("nav_Login").click()


@step("is redirected to login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Sign In"))


@step('mike clicks on "don\'t have account"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_name("user_signup").click()


@then("mike is redirected to signup form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Signup"))


@step("{name} enters correct username and password")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    users = User.objects.all()
    assert users.count() > 0
    assert_that(users,has_entries(User=name),"Username does not exist. Here are all users: {0}".format(users))
    username = User.objects.get(username=name)
    password = "password"

    login_form = context.driver.find_element_by_tag_name("form")

    username_element = login_form.find_element_by_name("username")
    username_element.send_keys(username)

    password_element = login_form.find_element_by_name("password")
    password_element.send_keys(password)

    login_form.submit()


@step("clicks on the sign in button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("charlie is redirected to dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("enoc enters incorrect username or password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("enoc clicks the sign in button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then('enoc is given message that states "incorrect username or password"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("login form is reloaded with blank username and password fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("mike does not have a nectr account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("charlie has a nectr student account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("brandon has a nectr student account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Juan has a nectr student account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("mike is not signed in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("mike clicks on join the hive")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("mike is redirected to login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("charlie is signed in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("charlie clicks on join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("charlie is redirected to join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("presented with join the hive application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("brandon is on join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("brandon does not complete application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("brandon clicks on submit button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("application is reloaded with information that has already been filled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("is incomplete fields are highlighted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("juan is on join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("juan completes application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("juan clicks on submit button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("juan is presened with success message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False
