#coding=utf-8
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
import time, os

success = True
desired_caps = {}
desired_caps['automationName'] = 'XCUITest'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.3.5'
desired_caps['deviceName'] = 'iPhone'
desired_caps['app'] = os.path.abspath('/Users/Jay/Downloads/pregnancy.ipa')
desired_caps['udid'] = 'baa8e87531d4a7bb7b1947e9c2c70df6762e3a6e'
#desired_caps['udid'] = 'd7d74757e2a04c8ec082d70c222cb781a8ddc799'
desired_caps['bundleId'] = 'com.gzmama.mama.PregnancyHelper'
#desired_caps['bundleId'] = 'com.apple.Health'
desired_caps['realDeviceLogger'] = '/Users/Jay/.nvm/versions/node/v5.9.0/lib/node_modules/deviceconsole'
desired_caps['autoAcceptAlerts'] = 'true'
#desired_caps['noReset'] = 'true'
print "start app"
wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)
print "start click"
wd.find_element_by_name(u"允许").click()
wd.find_element_by_name(u"好").click()
time.sleep(20)

wd.quit()
