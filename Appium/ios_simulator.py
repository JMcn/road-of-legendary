from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
import time, os

success = True
desired_caps = {}
desired_caps['automationName'] = 'XCUITest'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '10.1'
desired_caps['deviceName'] = 'iPhone 6s'
desired_caps['app'] = os.path.abspath('/Users/Jay/Downloads/PregnancyHelper.app')
#desired_caps['udid'] = 'baa8e87531d4a7bb7b1947e9c2c70df6762e3a6e'
#desired_caps['app'] = 'com.gzmama.mama.PregnancyHelper'
#desired_caps['realDeviceLogger'] = '/Users/Jay/.nvm/versions/node/v5.9.0/lib/node_modules/deviceconsole'
desired_caps['unicodeKeyboard'] = 'true'
desired_caps['autoAcceptAlerts'] = 'true'
desired_caps['fullReset'] = 'false'

wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)
wd.find_element_by_name('Allow').click()
time.sleep(20)

wd.quit()