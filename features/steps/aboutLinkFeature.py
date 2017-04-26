from behave import *

use_step_matcher("re")


@given("Mike is on nectr home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Mike scrolls down to links")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Mike should be redirected to "About" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
