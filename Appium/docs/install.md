# windows 环境安装教程
所需软件的百度云盘链接：https://pan.baidu.com/s/1dFFTy1b

## 目录：
* [Python 安装](#python-安装)
* [pip 安装](#pip-安装)
* [Robot Framework 安装](#robot-framework-安装)
* [ride 安装](#ride-安装)
* [Appium 安装](#appium-安装)

## Python 安装
首先，从[官网](https://www.python.org/)下载 最新版本 的 [Python 2.7](https://www.python.org/downloads/release/python-2712/)。可通过 Python 官网 的”Windows Installer”链接保证下载到的版本是最新的。`python-2.7.12.amd64.msi`

Windows版本是MSI文件格式，双击它即可开始安装。MSI文件格式允许Windows管理员使用标准工具自动 进行安装流程。

Python将安装到内含版本号信息的路径，例如2.7版本的 Python 将被安装到 C:\Python27\, 故多个版本的 Python 可以共存在一个系统里，不会有冲突。当然仅有一个默认的 Python 文件解释器， PATH 环境变量也不是自动修改的，开发人员可以控制要运行的Python 版本。

把默认使用的 Python 版本路径加到 PATH 环境变量中，避免每次使用时都要冗余地写全 Python  解释器路径。假设安装路径是 C:\Python27\, 将这段加入到 PATH 中:
```
C:\Python27\;C:\Python27\Scripts\
```

或在 powershell 中运行:
```
:SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
```

验证安装成功，在命令行输入：
```
python -V
```

![python](http://o84t5lcxv.bkt.clouddn.com/9d3d7c923ed89af9cae6c89d775889f7.png)

## pip 安装
下载 [pip 包](https://pypi.python.org/pypi/pip#downloads),`pip-8.1.2.tar.gz`，解压到一个文件夹，用CMD控制台进入解压目录，输入：
```
python setup.py install
```

验证安装成功，在命令行输入：
```
pip list
```

![pip](http://o84t5lcxv.bkt.clouddn.com/ac08efd6cf28cc9290b785cb4e62855e.png)

## Robot Framework 安装
利用 pip 安装，在命令行输入：
```
pip install robotframework==3.0
```

![robotframework](http://o84t5lcxv.bkt.clouddn.com/a2ec793dffad829444e55aebb08a0393.png)

## ride 安装
首先安装依赖 [wxPython](http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/)，`wxPython2.8-win64-unicode-2.8.12.1-py27.exe`

利用 pip 安装 ride：
```
pip install robotframework-ride
```

![ride](http://o84t5lcxv.bkt.clouddn.com/68d90c135533ecb247d4e992129fa044.png)

打开 ride 检查能否正常打开：
```
C:\Users\Jay>cd C:\Python27\Scripts
C:\Python27\Scripts>python ride.py
```

![ride.py](http://o84t5lcxv.bkt.clouddn.com/f1fdc6e01bbe5a9a70bc476e8c26cc2e.png)

附：[如何制作 RIDE 桌面图标](http://mp.weixin.qq.com/s?__biz=MjM5NTA3MDgyNg==&mid=2656981311&idx=1&sn=808ee83398b8fd2b8ceca30eb1b3d9e3&scene=19#wechat_redirect)

利用 pip 安装 robotframework-appiumlibrary
```
pip install robotframework-appiumlibrary
```

## Appium 安装

参考 [appium-girls 的文章](https://anikikun.gitbooks.io/appium-girls-tutorial/content/2_install_appium.html)

安装步骤

* [安装 JDK 并设置环境变量](#安装-jdk-并设置环境变量)
* [安装 Android SDK 并设置环境变量](#安装-android-sdk-并设置环境变量)
* [安装 Nodejs](#安装-nodejs)
* [安装 appium](#安装-appium)
* [验证安装](#验证安装)

### 安装 JDK 并设置环境变量
1. 到 Java 官网下载相应的 JDK 并安装，`jdk-7u79-windows-x64.exe`
2. 设置环境变量
	1. 添加 `JAVA_HOME` 对应的路径 `C:\Program Files\Java\jdk1.7.0_79`
	2. 在 `PATH` 变量末尾追加 `;%JAVA_HOME%\bin;`
	3. 添加 `CLASSPATH`，设置值为:`%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar`

设置完毕后在命令行输入
```
java -version
```

![java](http://o84t5lcxv.bkt.clouddn.com/354748ad102de91cdfb6ce49e4c7baac.png)

### 安装 Android SDK 并设置环境变量

1. 到 [Android 官网](https://developer.android.com/studio/index.html#downloads)下载并安装SDK,`installer_r24.4.1-windows.exe`

2. 设置环境变量
    1. 添加 `ANDROID_HOME` 设置值为：`C:\Program Files (x86)\Android\android-sdk`
    2. 在path环境变量值末尾追加：`;%ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools;`

安装完成后打开 Android SDK Manager

![sdkmanager](http://o84t5lcxv.bkt.clouddn.com/08bc1aa05e43f6f5f132b57c6cfd36da.png)

参考 http://androiddevtools.cn/ 使用国内 Android SDK 镜像源

使用方法：

1. 启动 Android SDK Manager ，打开主界面，依次选择「Tools」、「Options...」，弹出『Android SDK Manager - Settings』窗口；
2. 在『Android SDK Manager - Settings』窗口中，在「HTTP Proxy Server」和「HTTP Proxy Port」输入框内填入 `mirrors.neusoft.edu.cn `和 `80`，并且选中「Force https://... sources to be fetched using http://...」复选框。设置完成后单击「Close」按钮关闭『Android SDK Manager - Settings』窗口返回到主界面；
3. 依次选择「Packages」、「Reload」。

![proxy](http://o84t5lcxv.bkt.clouddn.com/0b346231986144d67ed2c97b54fc3212.png)

选择以下安卓组件下载安装

![sdk](http://o84t5lcxv.bkt.clouddn.com/177204c217dc29723559ae99711b3ff8.png)

### 安装 Nodejs
到 [Nodejs 官网](https://nodejs.org/en/download/)下载最新版本的 NodeJs 并直接安装,`node-v4.6.1-x64.msi`
安装完毕后，打开命令行，分别输入 `node -v`，`npm -v`，出现类似下面的信息说明安装成功。

![node](http://o84t5lcxv.bkt.clouddn.com/4ab1a02fa0ddf06563449046e47bd7a1.png)

### 安装 appium
安装appium有两种方式：

1. 使用 npm (Node js 的管理与分发工具)
2. 使用 Appium 官方安装包安装

> npm 安装在 windows 相对比较复杂，建议使用官方安装包。

#### 使用NPM安装Appium
首先，npm默认的镜像地址已经被墙，我们需要将npm的下载地址更改为国内的地址。
打开终端（命令行），输入
```
npm config get registry
```

我们可以看到当前 npm 的镜像地址。
我们需要将这个地址替换为国内的地址，这里我们替换成淘宝的NPM镜像源：
```
npm config set registry=https://registry.npm.taobao.org/
```

敲击回车后，我们再次输入
```
npm config get registry
```

可以确认镜像源是否替换成功。

升级 npm ，因为 appium 需要 npm > 3
```
npm install npm -g
```

接下来我们就可以安装Appium了：
```
npm install -g appium@1.5.3
```

> 需要注意的是，最新版本的Appium在安装过程中，会去google拉取最新的chromedriver，因为google被墙的关系，你很可能无法下载。这里强烈建议各位学习如何翻墙(openvpn)。

#### 使用Appium官方安装包安装
到 [Appium 官网](https://bitbucket.org/appium/appium.app/downloads/) 下载和你所使用系统一致的版本进行安装。`AppiumForWindows_1_4_16_1.zip`


### 验证安装
命令行安装 appium-doctor 可以检查环境是否正常
```
npm install -g appium-doctor
appium-doctor
```

执行 robotframework appium 孕育管家demo
```
appium --session-override
```

打开 ride.py 导入 rf-pregnancy 文件夹
修改 `全局配置.txt` 中的 `${PLATFORM_VERSION}` 和 `${DEVICE_NAME}`
运行一下。
