from behave import given, when, then
from time import sleep

@given('Click profile settings')

def click_on_profile_setting(context):
    context.app.setting_page.click_on_profile_setting()