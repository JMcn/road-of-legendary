#coding=utf-8
import wda
import time
# Enable debug will see http Request and Response
#wda.DEBUG = True
c = wda.Client('http://172.68.81.126:8100')
print c.status()
c.home()
#c.screenshot('screen1.png')
s=c.session('com.gzmama.mama.PregnancyHelper')
#print s.orientation
#print s.window_size()
#c.screenshot('screen2.png')
s(text=u"我的", className='Button').tap()
s(text=u"登录", className='Button').tap()
s(className='XCUIElementTypeTextField').set_text("15918854807")
s(className='XCUIElementTypeSecureTextField').set_text("a12345")
s(text=u"登录", className='Button').tap()
time.sleep(3)
s.swipe(150, 400, 150, 100)
setting = u"设置"
s(xpath="//XCUIElementTypeStaticText[@name='" + setting + "']").tap()
quit = u"退出"
s(xpath="//XCUIElementTypeStaticText[@name='" + quit + "']").tap()

