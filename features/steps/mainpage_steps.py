from behave import given, when, then
from time import sleep

@given('open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Click on settings option')
def click_settings(context):
    context.app.main_page.click_settings()