from pages.base_page import BasePage
from pages.profilepage_page import Profile
from pages.settings_page import Settings
from pages.main_page import Mainpage
from pages.sign_in_page import SignIn



class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.settings_page = Settings(driver)
        self.main_page = Mainpage(driver)
        self.sign_in_page = SignIn(driver)
        self.profilepage_page = Profile(driver)

