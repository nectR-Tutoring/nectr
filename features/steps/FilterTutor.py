from behave import *

use_step_matcher("re")


@step("Mike has not yet selected a tutor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("all tutors who tutor that subject will be displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("Mike clicks <subject> radio button on subject filter")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("all tutors who tutor <subject> will be displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("Mike clicks <dayOfTheWeek> radio button on availability filter")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("all tutors who tutor on that day will be displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@when("Mike wants to filter by hourly rate")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@then("Mike should be able to filter using a slider")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False


@given("Mike is on nectr web site")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(context.server_url)
