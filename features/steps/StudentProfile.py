from behave import *
from django.test import Client
from hamcrest import assert_that, is_, is_not

from nectr.users.tests.factories import UserFactory

use_step_matcher("parse")


@step("Mike is redirected to nectr dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Mike has nectr account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.curr_user = UserFactory(first_name="Mike")
    username = context.curr_user.username
    assert_that(username, is_not(None))



@then('"Hello <Mike\'s username>" is shown')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Mike can add information to dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Mike is on his dashboard page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "Edit" button on "personal information" section of dashboard')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then('Mike can edit or add information to "personal information"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "Edit" button on "contact information" section of dashboard')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then('Mike can edit or add information to "contact information"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "Edit" button on "communication preferences" section of dashboard')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then('Mike can edit or add information to "communication preferences"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Mike is signed into his nectr account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.curr_user.is_authenticated


@step("Mike is redirected to nectr profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Mike can add information to profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Mike is on his profile page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url + "/users/" + context.curr_user.username)


@when('Mike clicks on "{edit_button}" button on "personal information" section of profile')
def step_impl(context, edit_button):
    """
    :type edit_button: str
    :type context: behave.runner.Context
    """
    print(context.driver.page_source)
    c=Client()
    context.driver.find_element_by_name(edit_button)


@step("Mike's username is MikeAyoub")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step("Mike's password is JavaSucks123")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike is on his "Dashboard" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('title of page is "MikeAyoub" dashboard')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "My Profile" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "Edit" button on "personal information" section of his profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike clicks on "name" text field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike enters "Mike Ayoub"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike clicks "Save" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("Mike's personal information is saved to his profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("Mike's contact information is saved to his profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "Edit" button on "contact information" section of profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "Edit" button on "communication preferences" section of profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike clicks on "Student Class Level" text field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike enters "Senior"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('Mike clicks on "Edit" button on "contact information" section of his profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike clicks on "Email" text field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike enters "ayouf@farmingdale\.edu"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike clicks on "Phone number" text field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@step('Mike enters "6318735489"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False
