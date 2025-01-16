from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage
class SignIn(BasePage):
    EMAIL_TEXTBOX = (By.ID, "email-2")
    PSWD_TEXTBOX = (By.ID, "field")
    LOGIN_BUTTON = (By.CSS_SELECTOR,".login-button")

    def open_sign_in_page(self):
        self.open_url(
            'https://soft.reelly.io/sign-in')
        sleep(5)

    def click_sign_in_button(self):
        self.wait_and_click(*self.LOGIN_BUTTON)

    def enter_email(self):
        self.input_text('ratnasinha012@gmail.com', *self.EMAIL_TEXTBOX)

    def enter_password(self):
        self.input_text('Newjob24!', *self.PSWD_TEXTBOX)