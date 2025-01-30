from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context,scenario_name):
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(options=chrome_options,service=service)



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

"""driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
"""

### BROWSERSTACK ###
# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings