from behave import *

use_step_matcher("parse")


@given("I am in {project_root}")
def step_impl(context, project_root):
    """
    :type project_root: str
    :type context: behave.runner.Context
    """
    pass


@when('I run "docker-compose up"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("docker-compose should deploy to Docker")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
