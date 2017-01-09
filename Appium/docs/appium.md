# Appium 知识
参考教程：
* [Appium Girls学习指南](https://anikikun.gitbooks.io/appium-girls-tutorial/content/desired_caps.html)
* [官方Documentation](http://appium.io/slate/cn/master/?python#)
* [官方Tutorial](http://appium.io/tutorial.html?lang=zh)

示例代码：
* [appium/sample-code](https://github.com/appium/sample-code)

## 从命令行启动 Appium Server
```shell
$ appium
[Appium] Welcome to Appium v1.5.3
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

1. 表明目前启动的 appium 版本
2. 说明监听的地址及端口

## 常用 Server Argument 讲解
| 标志 | 默认值 | 描述 | 例子 |
| --- | --- | --- | --- |
| -a, --address	| 0.0.0.0 | 监听的 ip 地址。注意在图形化界面上默认值为 127.0.0.1 | --address 0.0.0.0 |
| -p, --port | 4723 | 监听的端口。需要启动多个 appium server 进行并行测试时需要保证每个 server 的监听端口不一样。| --port 4723 |
| --log-timestamp | false | 在日志输出里显示时间戳 | |
| --local-timezone | false | 在日志输出的时间戳使用本地时间 | |
| -g, --log | null | 将日志输出到指定文件 | --log /path/to/appium.log |
| --session-override | false | 允许 session 被覆盖 (冲突的话) | |
| --command-timeout | 60 | 默认所有会话的接收命令超时时间 (在超时时间内没有接收到新命令，自动关闭会话)。 会被新的超时时间覆盖 | |

这些参数同时可以在图形化界面上配置。

重新启动appium：

```shell
$ appium --address 0.0.0.0 --port 4723 --log "appium.log" --log-timestamp --local-timezone --session-override
```

## 学习 DesiredCapabilities
Desired Capabilities 携带了一些配置信息，在启动session的时候是必须提供，如启动模式、apk/app配置、package/activity配置、浏览器配置、键盘配置等。

| 关键字 | 描述 | 实例 |
| --- | --- | --- |
| platformName | 手机操作系统 | iOS,Android,FirefoxOS |
| platformVersion | 手机操作系统版本 | 例如： 7.1, 4.4 |
| deviceName | 手机类型或模拟器类型 | iPhone Simulator, iPad Simulator, Android Emulator, Galaxy S4等。在 iOS 上，这个关键字的值必须是使用 instruments -s devices 得到的可使用的设备名称之一。在 Android 上，这个关键字目前不起作用。 |
| app | .ipa 或者 .apk(也可以使是包含他们的zip)文件所在的本地绝对路径或者远程路径 | Appium会先尝试安装路径对应的应用在适当的真机或模拟器上。针对Android系统，如果你指定app-package和app-activity(具体见下面)的话，那么就可以不指定app。 |
| browserName | 需要进行自动化测试的手机 web 浏览器名称。如果是对应用进行自动化测试，这个关键字的值应为空。 | iOS 系统上可以用 ‘Safari‘ ，Android 系统上可以用 ‘Chrome‘, ‘Chromium‘, 或 ‘Browser‘。 |
| automationName | 自动化测试引擎 | Appium,Selendroid |
| appActivity | 要从应用包中启动的 Android Activity 名称。 | 它通常需要在前面添加 . (如：使用.MainActivity 而不是 MainActivity) MainActivity, .Settings |
| appPackage | 你想运行的Android应用的包名 | 比如com.example.android.myApp
| appWaitActivity | 你想要等待启动的 Android Activity 名称 |	SplashActivity |
| unicodeKeyboard | 是否在测试过程中切换到能支持多国语言输入的输入法 | true 表示是，false 表示否 |
| resetKeyboard | 是否在测试完成后自动切换回原有输入法 | true 表示是，false 表示否 |
| avd | 需要启动的 AVD (安卓虚拟设备) 名称。 | 如 api19 |
| noSign | 跳过检查和对应用进行 debug 签名的步骤。只能在使用 UiAutomator 时使用，使用 selendroid 是不行。默认值 false | true 或 false |

```python
class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.9.47:5555'
        desired_caps['avd'] = 'Nexus_6_API_22'
        desired_caps['app'] = PATH(
            '../../../sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
        )
```

## 移动手势的自动化
触摸操作 (TOUCHACTION)

TouchAction 对象包含一连串的事件。

在所有的appium客户端库中，触摸对象创建并给出一连串的事件。

规范中的可用事件有： * 短按 (press) * 释放 (release) * 移动到 (moveTo) * 点击 (tap) * 等待 (wait) * 长按 (longPress) * 取消 (cancel) * 执行 (perform)

这里有一个通过伪代码创建动作的例子：

`TouchAction().press(el0).moveTo(el1).release()`

上述模拟用户按下一个元素，滑动他的手指到另一个位置，然后从屏幕上释放其手指。

Appium按顺序执行这些事件。你可以添加一个 wait 事件来控制相应手势的时间。

appium客户端库有不同的方式来实现上述例子，比如：你可以传递一个坐标值或一个元素给 moveTo 事件。同时传递坐标和元素，会将坐标和元素对应起来，但这不是绝对的。

调用 perform 事件发送整个事件序列给appium，从而使触摸手势在设备上运行。

Appium客户端还允许人们直接通过驱动程序对象执行触摸操作, 而不是调用触摸操作对象的perform事件。

在伪代码中，以下两个是等价的：
`TouchAction().tap(el).perform()`

`driver.perform(TouchAction().tap(el))`


多点触控 (MULTITOUCH)

MultiTouch 对象是触摸操作的集合。

多点触控手势只有两个方法，添加 (add) 和执行 (perform) 。

add 用于将不同的触摸操作添加到一个多点触控中。

当 perform 被调用的时候，所有被添加到多点触摸中的触摸事件会被发送到appium并且被执行，就像它们同时发生一样。Appium会执行“触摸事件”中的第一个事件，然后第二个，以此类推。

用两只手指点击的代码示例：
```
action0 = TouchAction().tap(el)
action1 = TouchAction().tap(el)
MultiAction().add(action0).add(action1).perform()
```

robotframework 关键字：
* zoom
* pinch
* swipe
* scroll
* scroll_down
* scroll_up
* long_press
* tap
* click_a_point
* click_element_at_coordinates





