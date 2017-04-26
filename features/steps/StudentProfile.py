from behave import *

use_step_matcher("re")


@step("Mike is redirected to nectr profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Mike has nectr account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('"Hello <Mike\'s username>" is shown')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Mike can add information to profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Mike is on his profile page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Mike clicks on "Edit" button on "personal information" section of profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Mike can edit or add information to "personal information"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Mike clicks on "Edit" button on "contact information" section of profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Mike can edit or add information to "contact information"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('Mike clicks on "Edit" button on "communication preferences" section of profile')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Mike can edit or add information to "communication preferences"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
