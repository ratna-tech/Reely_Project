from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_signin(context):
    context.app.sign_in_page.open_sign_in_page()

@when('enter_email')
def enter_email(context):
    context.app.sign_in_page.enter_email()

@when('enter password')
def enter_password(context):
    context.app.sign_in_page.enter_password()

@when('click on signin button')
def click_signin(context):
    context.app.sign_in_page.click_sign_in_button()

