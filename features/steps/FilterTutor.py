from behave import *
from hamcrest import has_items
from hamcrest.core import assert_that, is_

from nectr.tutor.tests.factories import TutorFactory

use_step_matcher("parse")


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
    results = context.driver.find_elements_by_class_name('individual_tutor_result')
    print (results)
    assert_that(results, has_items)

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


@when('Mike enters "{course_name}"')
def step_impl(context, course_name):
    """
    :type course_name: str
    :type context: behave.runner.Context
    """
    search_bar = context.driver.find_element_by_name('search_text')
    search_bar.send_keys(course_name)
    tutor = TutorFactory(courses=course_name)
    print (tutor)
