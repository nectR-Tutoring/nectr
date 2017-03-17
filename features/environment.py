"""
behave environment module for testing behave-django
"""
import os
import django
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test"


def before_all(context):
    #context.base_url = "nectr.us"

    #context.localhost = "127.0.0.1"

    django.setup()

    from django.core.management import call_command
    call_command('flush', '--noinput')

    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()



def before_step(context, step):
    context.step_name = step


def before_feature(context, feature):
    if feature.name == 'Fixture loading':
        context.fixtures = ['behave-fixtures.json']


def before_scenario(context, scenario):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()
    if scenario.name == 'Load fixtures for this scenario and feature':
        context.fixtures.append('behave-second-fixture.json')


def after_scenario(context):
    context.test_case.tearDownClass()
    del context.test_case


def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()
