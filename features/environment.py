"""
behave environment module for testing behave-django
"""
from selenium.webdriver import Chrome


def before_all(context):
    context.base_url = "nectr.us"
    context.localhost = "127.0.0.1"
    context.browser.chrome = Chrome()


def after_all(context):
    context.browser.chrome.quit()
    context.browser.chrome = None


def before_step(context, step):
    context.step_name = step


def before_feature(context, feature):
    if feature.name == 'Fixture loading':
        context.fixtures = ['behave-fixtures.json']


def before_scenario(context, scenario):
    if scenario.name == 'Load fixtures for this scenario and feature':
        context.fixtures.append('behave-second-fixture.json')
