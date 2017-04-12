from behave import *

from features.factories import VisitorFactory

use_step_matcher("parse")


@given("{name} is not registered to nectr")
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    VisitorFactory(first_name=name)


@given("{name} is registered to nectr")
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    pass



@given("{name} is on nectr site")
def step_impl(context, name):
    """
    :param name: str ID of User using Name
    :type context: behave.runner.Context
    """
    br = context.browser
    br.visit(context.server_url + '/login/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()


@when("mike clicks on login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Mike will click on the button with id matching login



@step("is redirected to login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('mike clicks on "don\'t have account"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("mike is redirected to signup form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("charlie clicks on login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("charlie enters correct username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("clicks on the sign in button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("charlie is redirected to dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("enoc clicks on login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("enoc enters incorrect username or password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("enoc clicks the sign in button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('enoc is given message that states "incorrect username or password"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("login form is reloaded with blank username and password fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("mike does not have a nectr account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("charlie has a nectr student account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("brandon has a nectr student account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Juan has a nectr student account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("mike is not signed in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("mike clicks on join the hive")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("mike is redirected to login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("charlie is signed in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("charlie clicks on join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("charlie is redirected to join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("presented with join the hive application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("brandon is on join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("brandon does not complete application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("brandon clicks on submit button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("application is reloaded with information that has already been filled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("is incomplete fields are highlighted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("juan is on join the hive page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("juan completes application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("juan clicks on submit button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("juan is presened with success message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
