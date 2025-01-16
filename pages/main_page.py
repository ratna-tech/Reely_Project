from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage
class Mainpage(BasePage):

  SELECT_SETTING = (By.XPATH,"//div[text()='Settings']")
  PROFILE_SETTING = "a[href='/profile-edit']"


  def open_main_page(self):
      self.open_url('https://soft.reelly.io')


  def click_settings(self):
      self.wait_and_click(*self.SELECT_SETTING)
