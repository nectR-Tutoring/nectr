from behave import *
from hamcrest import *


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
