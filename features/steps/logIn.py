from behave import *
<<<<<<< HEAD
from hamcrest import assert_that, has_entries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.factories import VisitorFactory
from nectr.users.models import User
=======
from hamcrest import assert_that, contains_string, is_not, is_

from features.factories import VisitorFactory, RegisteredUserFactory
from nectr.users.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

>>>>>>> new_development
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
<<<<<<< HEAD
    UserFactory(username=name, password="password")
=======
    context.user = RegisteredUserFactory(first_name=name)
>>>>>>> new_development


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
<<<<<<< HEAD

    menu = context.wait.until(EC.element_to_be_clickable((By.NAME, "menu")))
    menu.click()

    context.driver.find_element_by_name("nav_Login").click()
=======
    context.driver.find_element_by_name(element_name).click()
>>>>>>> new_development


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
<<<<<<< HEAD
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Sign In"))
=======
    assert False

#
# @step("{name} clicks on the {element_type} button")
# def step_impl(context, element_type):
#     """
#     :type type: str
#     :type context: behave.runner.Context
#     """
#     context.driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
>>>>>>> new_development


@step("enoc enters incorrect username or assert Falseword")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
<<<<<<< HEAD
    context.driver.find_element_by_name("user_signup").click()
=======
    assert False
>>>>>>> new_development


@step("enoc clicks the sign in button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
<<<<<<< HEAD
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Signup"))


@step("{name} enters correct username and password")
def step_impl(context, name):
=======
    assert False


@then('enoc is given message that states "incorrect username or password"')
def step_impl(context):
>>>>>>> new_development
    """
    :type name: str
    :type context: behave.runner.Context
    """
<<<<<<< HEAD
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
=======
    assert False
>>>>>>> new_development


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
    # current_page_title = context.driver.title
    # assert_that(current_page_title, contains_string(title),
    #             "{0} Should be on {1} page".format(name, title))
    WebDriverWait(context.driver, 10).until(
        EC.title_contains('Login'))


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


@then("is redirected to login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("mike is redirected to signup form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("clicks on the sign in button")
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


@step("login form is reloaded with blank username and password fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Brandon is on home page of nectr")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url + "/")


@when('Brandon clicks "Menu"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    menu = context.driver.find_element_by_name('menu')
    menu.click()


@step('Brandon clicks "Log In" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_id('log-in-link').click()


@when("Brandon clicks on username text field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Brandon enters "Cashmeousside"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False
<<<<<<< HEAD
=======


@step("Brandon clicks on password text field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Brandon cicks "Sign In" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Brandon is not signed in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # TODO : Make this user logged out if it is logged in.
    pass


@step("Brandon's username is Cashmeousside")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Brandon's password is {password}")
def step_impl(context, password):
    """
    :type password: str
    :type context: behave.runner.Context
    """
    context.curr_user.set_password(password)


@step('title of the page is "Login"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.driver.title, is_('Login'))


@step('page contains an h1 whos text is "Sign In"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("Brandon is presented with an alert")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    h1 = context.driver.find_element_by_tag_name('h1')


@step("username text field is cleared")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("password text field is cleared")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("is redirected to login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Brandon enters "Howboudat"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Brandon enters "Howboudatt"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given('{name}\'s registered to nectR with username is "{username}"')
def step_impl(context, name, username):
    """
    :type name: str
    :type username: str
    :type context: behave.runner.Context
    """
    context.curr_user = UserFactory(username=username, first_name=name)
>>>>>>> new_development
