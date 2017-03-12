from behave import *

use_step_matcher("re")


@given("I am a visitor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('I go to "/"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('I should see the "Home Page"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('There should be a "Sign In" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('There should be a "Sign Up" link')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
