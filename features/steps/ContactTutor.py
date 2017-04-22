from behave import *

use_step_matcher("re")


@given("mike is on tutors profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('mike clicks "contact <tutor name>" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("mike will be redirected to message tutor form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("brandon is on tutors profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when('brandon clicks "contact <tutor name>" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("brandon will be redirected to sign up or sign in page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False
