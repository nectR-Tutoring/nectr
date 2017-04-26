from behave import *
from hamcrest import assert_that, contains_string
from features.factories import VisitorFactory, RegisteredUserFactory
from nectr.users.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    RegisteredUserFactory(first_name=name)


@given("{name} is on nectr site")
def step_impl(context, name):
    """
    :param name: str ID of User using Name
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url)


@step("{name} clicks on {element_name} button")
def step_impl(context, name, element_name):
    """
    :type element_name: str
    :type name: str
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_name(element_name).click()


@step('{name} clicks on "{html_element_link}"')
def step_impl(context, name, html_element_link):
    """
    :type name: str
    :type html_element_link: str
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_name(html_element_link).click()


@step("charlie enters correct username and assert Falseword")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False

#
# @step("{name} clicks on the {element_type} button")
# def step_impl(context, element_type):
#     """
#     :type type: str
#     :type context: behave.runner.Context
#     """
#     context.driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()


@step("enoc enters incorrect username or assert Falseword")
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


@step("login form is reloaded with blank username and assert Falseword fields")
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


@then("{name} is redirected to {title} page")
def step_impl(context, name, title):
    """
    :type title: str
    :type name: str
    :type context: behave.runner.Context
    """
    print(title)
    WebDriverWait(context.driver, 10).until(
        EC.title_contains(title))
    current_page_title = context.driver.title
    assert_that(current_page_title, contains_string(title),
                "{0} Should be on {1} page".format(name, title))


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


@step("charlie enters correct username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("{name} is redirected to dashboard")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    assert_that(context.driver.title.lower(), contains_string(name.lower()))


@when("{name} enters his correct username")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    user = User.objects.get(first_name__exact=name)
    username = user.get_username()
    e = context.driver.find_element_by_name("login")
    e.send_keys(username)


@step("{name} enters his correct password")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    user = User.objects.get(first_name__exact=name)
    user.set_password("password")
    e = context.driver.find_element_by_name("password")
    e.send_keys("password")


@step("mike clicks on login button on menu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('log-in-link').click()


@step("charlie clicks on login")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('log-in-link').click()


@step("Charlie clicks on sign in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_name(
        'login_button_form').click()
