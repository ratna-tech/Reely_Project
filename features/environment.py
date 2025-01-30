from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context,scenario_name):

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)




    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

""" driver_path = GeckoDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Firefox(service=service)

    ##HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )"""
""" bs_user = 'ratnasinha_y7CvZ9'
    bs_key = 'GJyz5rZdwLusiDrsqssy'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    options = Options()
    bstack_options = {
         "os" : "OS X",
         "osVersion" : "Monterey",
         'browserName': 'Firefox',
        'sessionName': scenario_name,
     }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)"""
### BROWSERSTACK ###
# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings