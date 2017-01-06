#coding=utf-8
import unittest
import time
import allure
from macaca import WebDriver
import os
import setting

class PregnancyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = WebDriver(setting.desired_caps, setting.server_url)
            cls.driver.init()
        except:
            cls.driver = WebDriver(setting.desired_caps_sim, setting.server_url)
            cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @allure.step(u'允许权限')
    def test_00_allow(self):
        try:
            self.driver.element_by_name("Allow").click()
        except:
            pass
        try:
            self.driver.element_by_name(u"允许").click()
        except:
            pass
        try:
            self.driver.element_by_name(u"好").click()
        except:
            pass

    @allure.step(u'启动页滑动')
    def test_01_login_swipe(self):
        self.driver.wait_for_element('xpath', '//XCUIElementTypePageIndicator[1]')
        for i in range(1, 5):
            self.driver.touch('drag', {'fromX': 300, 'fromY': 300, 'toX': 50, 'toY': 300, 'duration': 10})
        try:
            self.driver.wait_for_element('name', u"广州市")
            self.driver.element('name', u"广州市").click()
        except:
            pass
        finally:
            self.driver.wait_for_element('name', u"已有账号，立即登录")
            self.driver.element('name', u"已有账号，立即登录").click()

    @allure.step(u'登录账号')
    def test_02_login(self):
        login = u"登录"
        self.driver.wait_for_element('xpath', "//XCUIElementTypeButton[@name='" + login + "']")
        self.driver.element_by_xpath('//XCUIElementTypeTextField[1]').send_keys('15918854807')
        self.driver.element_by_xpath('//XCUIElementTypeSecureTextField[1]').send_keys('a12345')
        time.sleep(1)
        login = u"登录"
        self.driver.element_by_xpath("//XCUIElementTypeButton[@name='" + login + "']").click()
        time.sleep(3)
        try:
            self.driver.element_by_name('homePopupClose').click()
            self.driver.element_by_name(u"取消").click()
            self.driver.element_by_name(u"我的").click()
        except:
            pass

    @allure.step(u'退出账号')
    def test_03_logout(self):
        self.driver.element_by_name(u"圈子").click()
        self.driver.element_by_name(u"记录").click()
        self.driver.element_by_name(u"发现").click()
        self.driver.element_by_name(u"我的").click()
        self.driver.touch('drag', {'fromX': 150, 'fromY': 500, 'toX': 150, 'toY': 100, 'steps': 500})
        setting = u"设置"
        self.driver.element_by_xpath("//XCUIElementTypeStaticText[@name='" + setting + "']").click()
        quit = u"退出"
        self.driver.element_by_xpath("//XCUIElementTypeStaticText[@name='" + quit + "']").click()


if __name__ == '__main__':
    unittest.main()
