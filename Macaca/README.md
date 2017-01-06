# 孕育管家IOS UI TEST，基于 macaca 简单demo
来自阿里的开源项目: https://github.com/macacajs
Python Client binding for Macaca https://macacajs.github.io/wd.py

# 目录：

0. [requirements](#requirements)
0. [环境配置](#环境配置)
0. [脚本初始化参数](#脚本初始化参数)
0. [项目运行](#项目运行)


# requirements
* [python 2.7](https://www.python.org/) - 开发语言
* [wd](https://github.com/macacajs/wd.py)==0.1.5 Macaca python库

# 环境配置
## 安装 Node.js

请安装 [Node.js](https://nodejs.org/) v4.0 或者更高版本，装好 `Node.js` 后命令行里就已经集成了 `npm` 工具，为了提高安装模块的速度，请使用国内的 `cnpm`。

### iOS 环境

0. 请安装 Xcode8 或者更高版本
0. 需要安装 [usbmuxd](//github.com/libimobiledevice/usbmuxd) 以便于通过 USB 通道测试 iOS 真机，不需要测试真机则不用安装

```shell
$ brew install usbmuxd
```

0. 应用中如含有 WebView，请安装 [ios-webkit-debug-proxy](//github.com/google/ios-webkit-debug-proxy)

```shell
$ brew install ios-webkit-debug-proxy
```

备注：使用brew命令需要安装[Homebrew](http://brew.sh/index_zh-cn.html)（一款常用的 MacOS 的包管理器），请按照官网提示安装。

* 准备 App 包：如需要测试 iOS 应用，请使用 Scheme 设置为 debug 的 `.app` 包。

## 命令行工具

当前版本: [![NPM version][npm-image]][npm-url]

[npm-image]: https://img.shields.io/npm/v/macaca-cli.svg?style=flat-square
[npm-url]: https://npmjs.org/package/macaca-cli

### 全局安装

```shell
$ npm i -g macaca-cli
```

### 安装驱动（不同驱动适应不同平台的支持）

| 驱动       | 版本                                     | CI状态    |安装命令
| ---------- | ------------------ | ---------------------- | --------- |
| [Android](//github.com/macacajs/macaca-android)     | [![NPM version][npm-image-0]][npm-url-0] | [![build status][travis-image-0]][travis-url-0] 	|npm i macaca-android -g         |
| [Chrome](//github.com/macacajs/macaca-chrome)       | [![NPM version][npm-image-1]][npm-url-1] | [![build status][travis-image-1]][travis-url-1]  |npm i macaca-chrome -g          |
| [Electron](//github.com/macacajs/macaca-electron)   | [![NPM version][npm-image-2]][npm-url-2] | [![build status][travis-image-2]][travis-url-2] 	|npm i macaca-electron -g           |
| [iOS](//github.com/macacajs/macaca-ios)             | [![NPM version][npm-image-3]][npm-url-3] | [![build status][travis-image-3]][travis-url-3]  |npm i macaca-ios -g          |

[npm-image-0]: https://img.shields.io/npm/v/macaca-android.svg?style=flat-square
[npm-url-0]: https://npmjs.org/package/macaca-android
[npm-image-1]: https://img.shields.io/npm/v/macaca-chrome.svg?style=flat-square
[npm-url-1]: https://npmjs.org/package/macaca-chrome
[npm-image-2]: https://img.shields.io/npm/v/macaca-electron.svg?style=flat-square
[npm-url-2]: https://npmjs.org/package/macaca-electron
[npm-image-3]: https://img.shields.io/npm/v/macaca-ios.svg?style=flat-square
[npm-url-3]: https://npmjs.org/package/macaca-ios

[travis-image-0]: https://img.shields.io/travis/macacajs/macaca-android.svg?style=flat-square
[travis-url-0]: https://travis-ci.org/macacajs/macaca-android
[travis-image-1]: https://img.shields.io/travis/macacajs/macaca-chrome.svg?style=flat-square
[travis-url-1]: https://travis-ci.org/macacajs/macaca-chrome
[travis-image-2]: https://img.shields.io/travis/macacajs/macaca-electron.svg?style=flat-square
[travis-url-2]: https://travis-ci.org/macacajs/macaca-electron
[travis-image-3]: https://img.shields.io/travis/macacajs/macaca-ios.svg?style=flat-square
[travis-url-3]: https://travis-ci.org/macacajs/macaca-ios

上述驱动可以按照自身需要选择性的安装，比如只需要测试 iOS平台用例，就执行iOS的安装命令：

```shell
$ npm i macaca-ios -g
```

### 环境检查

通过 `macaca doctor` 可以检查环境是否配置成功

```shell
$ macaca doctor
```

如下图所示则表示环境均配置正常，如果有标红提示，则需要对应处理。

![macaca-doctor](http://ww1.sinaimg.cn/large/6b65a607jw1fa3cqjexk2j21c20padqa.jpg)

# 脚本初始化参数

Desired Capabilities 是用来在启动时配置服务器的参数。

## 基本用法

```javascript
const wd = require('macaca-wd');
const driver = wd.promiseChainRemote({
  host: 'localhost',
  port: 3456
});

const desiredCaps = {
  platformName: 'ios',
  deviceName: 'iPhone 6s',
  app: 'path/to/app'
}

driver.init(desiredCaps);
```

## 常见的参数

| 键     | 类型                                  | 描述    |
| ---------- | ---------------------------------------- | --------- |
| platformName | String | 当前用例运行的平台 { iOS / Android / Desktop } |
| browserName | String | 当前测试的浏览器名称 { iOS: Safari } { Android: Chrome } { Desktop: Chrome / Electron } |

## App 相关参数

| 键     | 类型                                  | 描述    |
| ---------- | ---------------------------------------- | --------- |
| deviceName | String | 模拟器的名称，例如 'iPhone 6' 或者 'Nexus 5x'。 |
| app | Stirng | .ipa，.app 或者 .apk 文件的绝对地址或者远程地址，或者是包含上述文件格式的 Zip 文件。 |
| udid | String | 测试设备的唯一设备 ID。|

## Android 的参数介绍

| 键     | 类型                                  | 描述    |
| ---------- | ---------------------------------------- | --------- |
| reuse | Number | 0: 启动并安装 app。1 (默认): 卸载并重装 app。 2: 仅重装 app。3: 在测试结束后保持 app 状态。|
| package | String | Android app 的 package name。 |
| activity | String | 启动时的 Activity name。|

## iOS 的参数介绍

| 键     | 类型                                  | 描述    |
| ---------- | ---------------------------------------- | --------- |
| reuse | Number | 0: 清楚数据并重装 app。 1: (默认) 卸载并重装 app。 2: 仅重装 app。 3: 在测试结束后保持 app 状态。 |
| bundleId | String | 应用的 Bundle ID，例如 com.apple.Maps。|
| autoAcceptAlerts | Boolean | 自动接受所有的系统弹窗信息。默认是 false。|
| autoDismissAlerts | Boolean | 自动拒绝所有的系统弹窗信息。默认是 false。|

# allure
## 用例修饰
添加 allure 装饰器的标记，用法参考：[allure-python](https://github.com/allure-framework/allure-python)

## allure 工具配置
安装pytest：`pip install pytest`
安装pip库：`pip install pytest-allure-adaptor`
[allure 压缩包](https://github.com/allure-framework/allure1/releases)解压，将/bin/allure 加入环境变量

# 项目运行
用例执行：
```
$ macaca server --verbose
$ py.test login.py --alluredir result
```

生成allure报告并查看：
```
$ allure generate result
$ allure report open
```

在jenkins中集成，使用 [Allure Jenkins Plugin](http://wiki.qatools.ru/display/AL/Allure+Jenkins+Plugin)