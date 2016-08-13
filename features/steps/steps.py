

from behave import *


@when('I go to home')
def step(context):
    context.browser.get('http://localhost:8000')


@then("it should have the title 'Welcome to Django'")
def step(context):
    assert context.browser.title == 'Welcome to Django'
