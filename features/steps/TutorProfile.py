from behave import *

use_step_matcher("re")


@given("Mike is a nect tutor and has already established student profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Mike is on tutor interface")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Mike can add information to his profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Mike is on his tutor profile page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Mike clicks on "Edit" button on "About Me" section of tutor profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Mike can edit his about me")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Mike can edit or add courses and subjects he offers tutoring in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Mike can edit or add his days and times he is available")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Mike can update the price he charges for tutoring")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Mike clicks on "Edit" button on "subjects taught" section of tutor profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Mike clicks on "Edit" button on "availability" section of tutor profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Mike clicks on "Edit" button on "Pricing" section of tutor profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
