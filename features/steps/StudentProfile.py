from behave import *
from hamcrest import assert_that, is_, is_not

from nectr.users.tests.factories import UserFactory

use_step_matcher("re")


@step("Mike is redirected to nectr profile")
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
    assert False


@when('Mike clicks on "Edit" button on "personal information" section of profile')
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


@when('Mike clicks on "Edit" button on "contact information" section of profile')
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


@when('Mike clicks on "Edit" button on "communication preferences" section of profile')
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
