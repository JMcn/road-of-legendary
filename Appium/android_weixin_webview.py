#coding=UTF-8
import os
from time import sleep
import unittest
from appium import webdriver

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
            'androidProcess' : 'com.tencent.mm:tools'
                }
            }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_webview(self):
        #操作: 进入微信搜索 滴滴公交查询
        # self.driver.find_element_by_android_uiautomator('new UiSelector().description("搜索")').click()
        # self.driver.find_element_by_id("com.tencent.mm:id/gn").send_keys(u'小程序示例')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发现']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='小程序']").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("搜索")').click()
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(u'滴滴公交查询')
        os.popen('adb shell ime set com.meizu.flyme.input/com.meizu.input.MzInputService')
        self.driver.find_element_by_class_name('android.widget.EditText').click()
        os.popen('adb shell input keyevent 66')
        print(self.driver.contexts)
        print self.driver.context
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print self.driver.context
        print 'success'
        print self.driver.page_source
        self.driver.find_element_by_class_name('search_item_inner').click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
