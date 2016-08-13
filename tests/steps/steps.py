

from behave import *


@when('I go to home')
def step(context):
    context.browser.get('http://localhost:8000')
    raise NotImplementedError(u'STEP: When I go to home')

@then("it should have the title 'Welcome to Django'")
def step(context):
    assert context.browser.title == 'Welcome to Django'
    raise NotImplementedError(u'STEP: Then it should have the title "Welcome to Django"')
