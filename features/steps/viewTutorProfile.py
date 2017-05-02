from behave import *

use_step_matcher("re")


@given("mike is on search results page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("mike is redirected to tutors dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('mike will see a "contact tutor" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("brandon is on search results page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("brandon is redirected to tutors dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('brandon will see a "sign in to contact tutor" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("mike is redirected to tutors profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("brandon is redirected to tutors profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
