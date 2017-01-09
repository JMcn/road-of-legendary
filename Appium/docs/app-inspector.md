# 查找app元素
## 工具介绍
1. uiautomatorviewer
2. [app-inspector](https://macacajs.github.io/app-inspector/cn/)

## uiautomatorviewer
安装完 android SDK，配置好环境变量

将 sdk 目录下的 `tools/lib/uiautomatorviewer.jar` 替换成能修改版的 [uiautomatorviewer.jar](https://pan.baidu.com/s/1dEGZQ1b)，能显示 xpath

在命令行 输入 `uiautomatorviewer` 可以进入查看app元素

## app-inspector
安装：
```
npm install macaca-cli -g
macaca doctor
npm install app-inspector -g
```

查看设备号：
`adb devices`

使用：
`app-inspector -u YOUR-DEVICE-ID`
然后在浏览器里面打开输出的链接：http://192.168.10.100:5678。推荐用 Chrome 浏览器。

## 定位方式
```
id=cn.mama.pregnant:id/iv_search
xpath=//*[contains(@text,'热点')]
xpath=//android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]
坐标
```
参考文章：https://testerhome.com/topics/5036

## web页的元素
在安卓手机安装 chrome 浏览器安卓版，连接到电脑，在电脑的 chrome 浏览器中地址栏输入：`chrome://inspect/`

![chrome-inspect](http://o84t5lcxv.bkt.clouddn.com/dcec754a3fef11522fd2169662ed2b07.png)