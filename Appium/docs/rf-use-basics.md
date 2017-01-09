# Robot Framework 使用基础

## robotframework 的文件格式

支持 HTML、TSV、Plain text、reStructuredText
我们选择 纯文本(Plain text/.txt) 作为项目的文件格式

## 纯文本 Plain text 的格式说明
在纯文本格式中可以使用两个或多个空格（建议4个空格）以及前后有空格的管道字符( | )来进行数据的分割，

在所有用例的测试数据表格中，前面必须有 1 个或多个星号（例如： `*** Settings ***` 或 `*Settings` ），并且在第一个表格之前的一切会被忽略。

![pipe](http://o84t5lcxv.bkt.clouddn.com/a7e965f5035477162a2b043432217fb9.png)

![txt](http://o84t5lcxv.bkt.clouddn.com/9a9e95d578064e6dae77c6db73b4f5b3.png)

## 测试数据表格
测试数据被组织在以下四种表格中。这些测试数据表格通过表格的第一个单元格被识别。

| 名称 | 作用 |
|--------|--------|
| Settings | 1)导入测试库，资源文件和变量文件 <br> 2)为测试集和测试用例定义元数据|
| Variables | 定义可以用在其他地方的测试数据的变量。 |
| Test Cases | 通过可用的关键字创建测试用例。 |
| Keywords | 通过低级别关键字创建用户自定义关键字 |

## 项目层次

`页面元素` -> `关键字` -> `测试套件`

`Variables` -> `Keywords` -> `Test Cases`

其中，初步是：页面元素按 app 的页面分，关键字和测试套件按模块分

## Settings
对用例、关键字等进行预先的设置，包含import、注释说明、setup、teardown等功能

引入 robotframework 库：
`Library    AppiumLibrary`

引入 其他文件资源：
`Resource    ..${/}全局配置.txt`

添加说明文档：
`Documentation    包括APP启动、关闭，一些服务关键字的设置`

设置 tag:
`Default Tags    初始化    APP`

测试数据的准备和清理：
`Suite Setup    打开APP`

`Suite Teardown    关闭APP`

## Variables
数据的类型分别用 $,@,&,% 表示

| 类型 | 表示 |
|--------|--------|
| scalars 标量 | ${SCALAR} |
| lists 列表 | @{LIST} |
| dictionaries 字典 | &{DICT} |
| environment variables 环境变量 | %{ENV_VAR} |

定义变量和值：
`${REMOTE_URL}    http://127.0.0.1:4723/wd/hub`

## Keywords
关键字，分为robotframework库的关键字（低级关键字）和 用户自定义关键字
库的关键字。
如 robotframework 自带的库：
`Builtln` 中的 `should_contain`
`DateTime` 中的 `get_current_date`

用户自定义关键字，其实就是定义在 `*** Keywords ***` 下的关键字：
```
关闭APP
    Close Application
```

## Test Cases
在 `*** Settings ***` 中引入含有库关键字or用户关键字的文件，并将一系列关键字步骤进行组合

```
进入登录页
    启动页滑动
    选择城市
    转跳到登录页
```

关键字不区分大小写，单词之间的 `_` 和空格可以相互替代
`should_contain` 等价于 `should contain` / `should_contain` / `SHOULD CONTAIN` / `SHOULD_CONTAIN`

## 在 pycharm 中查询关键字
因为安装了 IntelliBot 插件，所以长按 control 并点击关键字名称，可以转跳到相应的定义关键字所在文件

输入一些字符后，可以自动补全关键字

在系统的pip库文件夹中，可以找到相应的库和关键字

## 关键的 appium 启动 app 介绍
[关键字/APP初始化关键字.txt](../关键字/APP初始化关键字.txt)

参考 [Appium server capabilities](http://appium.io/slate/en/master/?java#appium-server-capabilities)

## 手势关键字
[关键字/手势关键字.txt](../关键字/手势关键字.txt)
按照屏幕大小，用相对坐标来表示滑动的开始和结束坐标，同时需要定义获取屏幕大小的用户关键字