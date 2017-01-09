# robotframework + appium

## robotframework

### 介绍
Robot Framework 是一种基于 Python 的可扩展关键字驱动自动化测试框架,通常用于端到端的可接收测试和可接收测试驱动的开发。可以用于测试声明涉及到多种技术和接口的分布式的,异构的应用系统。

### 高层架构

![robot](http://robotframework.org/robotframework/latest/images/architecture.png)

测试数据以一种简单易于编辑的表格格式。当 Robot Framework 启动的时候,启动测试数据,执行测试用例 并且生成日志和报告。核心框架不知道任何关于被测目标系统的细节,核心框架句柄与被测系统通过测试 库进行交互。测试库能够直接使用应用程序接口或者使用更低层次的测试工具作为驱动。

## appium
### 工作原理
Android 支持上, 在新版本的 Android 使用了 Uiautomator 框架,老版本的 android 上使用了 Selendroid。
Appium 驱动 Apple的 UIAutomation 库提供 IOS 支持。

![appium](http://std.mama.cn/testGroup/appium_share/raw/master/1.png)

### AppiumLibrary
AppiumLibrary is an appium testing library for RobotFramework
https://github.com/serhatbolsu/robotframework-appiumlibrary

## python
使用 2.7 版本，对 robotframework 支持最好，robotframework 在 3.0 版本才开始支持 python 3

## 工具以及开源项目组成
* [python 2.7](https://www.python.org/) - 开发语言
* [Appium](http://appium.io/) - 移动端测试框架
* [Robot Framework](http://robotframework.org/) - 关键字驱动测试框架
* [robotframework-appiumlibrary](https://github.com/serhatbolsu/robotframework-appiumlibrary) - RF扩展库
* [robotframework-ride](https://github.com/robotframework/RIDE) - RF图形化编辑器
* [app-inspector](https://macacajs.github.io/app-inspector/cn/) - 浏览器端的移动设备 UI 查看器
* [SimpleRegex/SRL-Python](https://github.com/SimpleRegex/SRL-Python) - python 简化正则匹配

## pip库的安装
```
pip install Appium-Python-Client==0.22
pip install robotframework==3.0
pip install robotframework-appiumlibrary==1.3.7
pip install robotframework-ride==2.0a1
```

## ride
图形界面的robotframework用例编写工具

## pycharm robotframework插件
[pycharm插件](http://www.daveze.cc/2016/05/05/%E5%9C%A8pycharm%E4%B8%AD%E6%94%AF%E6%8C%81robotframework%E8%84%9A%E6%9C%AC/)