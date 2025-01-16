from behave import given, when, then
from time import sleep

@when('Click on Edit profile option')
def click_on_profile_setting(context):
    context.app.profilepage_page.click_on_profile_setting()

@when('Enter {language} in the language input field')
def enter_some_test_information(context, language):
    context.app.profilepage_page.enter_some_test_information(language)

@then('Check language {language} is present in the input field')
def check_language(context, language):
    context.app.profilepage_page.check_language(language)

@then('Click on save changes button')
def click_on_save_changes(context):
    context.app.profilepage_page.click_on_save_changes()

@then('Click on close button')
def click_on_close(context):
    context.app.profilepage_page.close_button()
