from behave import *
from features.factories import VisitorFactory
from hamcrest import *

use_step_matcher("parse")


@given("I am a visitor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # context.visitor = VisitorFactory()
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
