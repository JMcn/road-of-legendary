#coding=UTF-8
import os
from time import sleep
import unittest
from appium import webdriver
import selenium

class ComplexAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'noReset': 'true',
            'deviceName': 'Android',
            'version':'5.1',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            #'autoWebview': 'true',
            #'recreatechromedriversessions':'True',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'fastReset': 'false',
            'chromeOptions': {
            'androidProcess' : 'com.tencent.mm:appbrand3'
                }
            }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_xiaochengxu(self):
        #操作: 进入微信小程序 滴滴公交查询
        # self.driver.find_element_by_android_uiautomator('new UiSelector().description("搜索")').click()
        # self.driver.find_element_by_id("com.tencent.mm:id/gn").send_keys(u'小程序示例')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发现']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='小程序']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='滴滴公交查询']").click()
        sleep(5)
        print self.driver.contexts
        print self.driver.context
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand3')
        print 'success'
        source = self.driver.page_source
        print source
        assert u"查公交用滴滴 看得见的精准" in source
        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
