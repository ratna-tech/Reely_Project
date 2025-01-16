from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage
class Profile(BasePage):


  PROFILE_SETTING = (By.CSS_SELECTOR,"a[href='/profile-edit']")
  LANGUAGE_TEXTBOX= (By.ID,"Languages")
  SAVE_AND_CLOSE_BUTTON= (By.CSS_SELECTOR,'.save-changes-button')
  CLOSE_BUTTON= (By.CSS_SELECTOR,'.close-button')
  def click_on_profile_setting(self):
      self.wait_and_click(*self.PROFILE_SETTING)

  def enter_some_test_information(self,language):
      self.find_element(*self.LANGUAGE_TEXTBOX).clear()
      self.input_text(language, *self.LANGUAGE_TEXTBOX)

  def check_language(self,language):
      language_element =self.find_element(*self.LANGUAGE_TEXTBOX)
      actual_text = language_element.get_attribute('value')
      print(actual_text)
      assert actual_text == language, f'Expected {language}, but got {actual_text}'

  def click_on_save_changes(self):
      self.wait_and_click(*self.SAVE_AND_CLOSE_BUTTON)

  def close_button(self):
      self.wait_and_click(*self.CLOSE_BUTTON)

