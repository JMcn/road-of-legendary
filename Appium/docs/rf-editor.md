# robotframework 的编辑器
1. [RIDE](https://github.com/robotframework/RIDE)
2. Pycharm 插件 [IntelliBot](https://plugins.jetbrains.com/plugin/7386?pr=idea)

## 安装 Pycharm
下载并安装 [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)，Professional 版功能全需要激活，激活可以参考 http://idea.qinxi1992.cn/ ，激活时选择 License server 填入在线激活服务器地址（或自建激活服务器参考 [IntelliJ License Server docker 版](http://pjoc.pub/docker-nginx-idea-license-serverda-jian-intellij-license-server/)）。

## 安装插件 IntelliBot
参考文章：[在pycharm中支持robotframework脚本](http://www.daveze.cc/2016/05/05/在pycharm中支持robotframework脚本/)

1. 打开Pyhcarm，打开菜单栏>Perferences>打开Plugins>点击Browse reponsitories
2. 输入IntelliBot，搜索并安装
3. 安装后，重启pycharm，打开任意.robot格式的脚本，正常应该可以识别了
4. 但是会发现，第一次安装，并不支持.txt格式的脚本文件，此时需要这么做：

- 4.1.打开Perferences>Editor>File Types>找到Robot Feature>在Registered Patterns中添加.txt
- 4.2.保存即可

5. 此时可以方便地编写脚本，支持自动补全，关键字跳转等。

## 配置运行测试命令
1. 脚本编写好了，想执行测试怎么办？可以用pybot命令直接在Pycharm的Terminal中执行。
2. 也有更方便的办法：不每次输入命令，每次直接在脚本中选择用例或suite直接执行

- 2.1.配置选择执行单个case：打开Perferences，在Tools中选择External Tools，点击+号新建，按如下信息配置：

![testcase](http://o84t5lcxv.bkt.clouddn.com/adb5bbcae4725d650f57eabb14435987.png)

- 2.2.配置执行testsuite

![testsuite](http://o84t5lcxv.bkt.clouddn.com/df342e08a92afc0c4477d27ace4ca6f1.png)

- 2.3.配置执行所选Tag

![tag](http://o84t5lcxv.bkt.clouddn.com/289b77d43d09d5d7b88bb7663e2cfa0c.png)

- 2.4.配置执行文件夹中的所有用例

![testsuites](http://o84t5lcxv.bkt.clouddn.com/7e270eb8886d830ec08ebdf69b1bccb4.png)

3.执行用例时，需要划选整个testcase名称执行单个case；选择testsuite文件或点击testsuite文件空白处执行整个testsuite；选择整个文件夹执行所有用例。