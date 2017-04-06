from behave import *
from wheel.signatures import assertTrue

use_step_matcher("re")


@given("Charlie is not yet registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Mike is not yet registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Enoc is not yet registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Brandon is not yet registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Juan is not yet registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Charlie is on the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Charlie clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('is asked "are you a farmingdale student"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("he says no")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('he is redirected to the "not a farmingdale student" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Mike is on the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("mike clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("he says yes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('he is redirected to the "sign up form"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Enoc is on the seacrch the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("enoc clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('is redirected to the "sign up" form')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("brandon is on the about nectr page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("brandon clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("juan is on the how it works page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("juan clicks on sign up link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
