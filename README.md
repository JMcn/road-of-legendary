# Road 0f Legendary
做更好的自己！加油!

# 技能树点亮

参考[移动无线测试技能图谱](https://github.com/TeamStuQ/skill-map/edit/master/data/map-MobileWirelessTesting.md)

## 常用IDE
- Android
	* ADT
	* Android Studio
- iOS
	* Xcode
- Common
	* Atom
	* Sublime Text
	* Vim
	* Visual Studio Code

## 基础知识
- Android
	* 掌握Android开发基础技能
- iOS
	* 掌握iOS开发基础技能
- Web
	* 掌握Web开发基础技能
- api
	* 掌握api相关基础知识
- 测试
	* 掌握基本的测试用例设计方法和思想

## 常见应用模式
- Native
- Hybrid
- H5 App
- ReactNative

## 常用工具
- Android
	* Android sdk manager
	* adb
	* ddms
	* ant
	* aapt
	* emulator
	* Genymotion
	* hierarchyviewer
	* monitor
	* monkey
	* monkeyrunner
	* uiautomatorviewer
- iOS
	* lldb
	* iExplorer
	* libimobiledevice 套件
	* codesign
	* instruments
	* xcodebuild
	* atos
	* xcrun

## 常用UI Automation框架
- Android
	* Instrumentation
	* Athrun
	* Robotium
	* Monkey
	* Monkeyrunner
	* uiautomator
	* Selendroid
	* Calabash*Android
	* monkeytalk
	* Appium  √	
   * Espresso
	* cafe
- iOS
	* UIAutomation(旧)
	* XCUITesting
	* KIF
	* Frank
	* Appium
	* ios-driver
	* Mechanic.js
	* monkeytalk
	* Calabash*iOS
	* TuneupJs
	* ynm3k
- Appium
- Macaca


## 常用单元测试框架
- Android
	* robolectric
	* Instrumentation
	* Mockito
	* RxJava
- iOS
	* OCUnit
	* GHUnit
	* XCTest
	* OCMock
	* OCMockito
	* Expecta
	* OCHamcrest

## 常用动态更新
- ReactNative
- waxpatch/wax
- ota

## 常用性能工具

### 抓包
- Charles
- fiddler
- burpsuites
- tcpdump
- anyproxy

### 弱网模拟
- iOS developer mode
- ATC
- Charles

### memory
- Android
	* MAT
	* ddms
	* Memory Monitor
	* Allocation Tracker
	* LeakCanary
	* dumpsys
	* procrank
	* top
- iOS
	* Memory Leaks

### Scan
- Android
	* findbugs
	* lint
	* infer
	* CheckStyle
	* PMD
- iOS
	* scan*build
	* oclint
	* infer
	* deployment

### other
- Common
	* 安捷伦
	* tcpdump
	* wireshark
	* 高速(慢速)摄像机
	* 埋点
	* 腾讯GT
	* 网易Emmagee
- Android
	* gfxinfo
	* dumpsys
	* traceview
	* systrace
	* GameBench
	* battery*historian
- iOS
	* Core Animation(instruments)
	* Network(instruments)
	* TimeProfiler(instruments)
	* Zombies(instruments)

## 安全
- Android
	* Drozer
	* apktool
	* dex2jar
	* proguard
	* 加固
	* exported/permission
	* AndBug
	* androguard
	* Xposed

- iOS
	* IDB
	* iRET
	* DVIA
	* LibiMobileDevice
	* otool

## 覆盖率
- Android
    - Jacoco
    - EMMA
- iOS
    - gcov

## 动态更新
- Android
    - Dexposed（二次开发之后）
    - Robust
    - android-frontia
    - Nuwa
    - HotFix
    - RocooFix
    - DroidFix
    - AndFix
- iOS
    - JSPatch
    - WaxPatch
- ota
- ReactNative
- weex

## abtest
- AB Tester
- AppAdhocOptimizer
- Google Website Optimizer
- Visual Website Optimizer

## 常用灰度测试工具
- testflight
- 蒲公英
- fir
- pre

## 常用云测平台
- testin
- MQC
- MTC

## 常用持续集成平台／相关工具
- Jenkins
- Travis CI
- Android
	* mvn
	* gradle
- iOS
	* xctool
	* Cocoapods

## 多语言开发应用
- SL4A
- gomobile

## 多设备远程管理平台
- STF

## 自动遍历工具
- AppCrawle

## 软技能
- 知识管理/总结分享
- 沟通技巧/团队协作
- 需求管理/PM
- 交互设计/可用性/可访问性知识
- 快速的学习能力

--------
参考[测试体系](https://testerhome.com/topics/2940)

#测试技术

## 云测服务使用
- mtc
- testin
- fir
- mqc

## UI自动化
- appium
- capybara
- selenium
- phantomjs(推荐)

## 接口测试
- 框架选择
	* soapui
	* capybara-json
	* gatling
	* 参考他的集成测试例子
- fake server
- 分析工具
	* fiddler(貌似是唯一可自动解码工具)
	* soapui
	* em-proxy
	* 自定义代理
- 单元测试
	* 研发推进, 仅作支持
	* 持续集成结合
	* 静态扫描
		- findbugs

## 性能测试
- 负载测试
- 加压工具
	* gatling
	* ab
	* jmeter
- 监控平台
	* influxdb+grafana
	* ELK
	* nmon(不推荐)
- 性能剖析
	* byteman
	* btrace
	* 火焰图
		- perfj
		- systemtap
## 测试分析体系
- 覆盖率
	* jacoco
- 流程建模
	* 根据byteman构建思维导图
- 代码diff
	* 思维导图红黑线diff
	* dot绘图
- debug与trace

## 研发流程
- jenkins持续集成
	* 自动构建
		- 发布包构建
		- docker镜像构建
	* 自动编译
	* 自动静态扫描
	* 单测
	* 部署
	* 性能测试
	* 接口测试
	* UI测试
	* 报警机制
		- 大job收集所有子job的结果
		- 邮件提醒为主
- 手工测试
	* 新功能测试
	* 预发布环境
	* 预演环境
		- testerhome的引流
- 开发模式
	* 分支开发主干发布
	* 基于每个分支构建对应的持续集成job
	* 发布版本从tag中获取
	* 持续集成监控tag

## 测试环境
- 手工部署
- 自动化部署
	* docker
		- 基础镜像可以手工构建
		- 给每个容器分配独立的ip
	* vagrant
	* vmware virtualbox

##线上环境
- 接口版本化
- 灰度发布
- 流量旁路

# 翻译计划
robotframework 官方文档

# 2017读50本书

备选书单：
技术类：

0. Python学习手册(第4版)
0. 失控
0. 深入理解Android自动化测试
0. Android应用测试与调试实战
0. 移动App性能评测与优化
0. 腾讯Android自动化测试实战
0. 白帽子讲 Web 安全
0. 测试驱动开发
0. 测试驱动开发的艺术
0. 持续集成软件质量改进和风险降低之道
0. 持续交付-发布可靠软件的系统方法
0. 大话移动APP测试 Android与iOS应用测试指南
0. 疯狂Android讲义
0. 高级软件测试卷1：高级软件测试分析师
0. 高级软件测试卷2：高级软件测试经理
0. 高性能Linux服务器构建实战：运维监控、性能调优与集群应用
0. 计算机网络（第5版）（美）特南鲍姆
0. 零成本实现Web性能测试：基于Apache JMeter
0. 敏捷软件测试：测试人员与敏捷团队的实践指南
0. 轻轻松松自动化测试
0. 软测之魂：核心测试设计精解
0. 软件测试的艺术
0. 软件测试经验与教训
0. 软件测试与持续质量改进
0. 软件测试自动化
0. 软件测试自动化技术与实例详解
0. 软件架构模式
0. 深入理解计算机系统
0. 探索式测试实践之路
0. 淘宝技术这十年
0. 完美测试
0. 网络营销其实很简单—15位业界知名专家布道互联网络营销
0. 微软的软件测试之道
0. 悟透JAVASCRIPT.美绘本
0. 细说PHP(第2版)
0. 笑傲测试 软件测试流程方法与实施
0. 移动App测试实战 顶级互联网企业软件测试和质量提升最佳实践
0. 捉虫记 大容量Web应用性能测试与LoadRunner实战
0. HTTP权威指南
0. iOS测试指南
0. JavaScript高级编程3
0. jenkins权威指南 英文版
0. Node.js开发指南
0. Python Web开发：测试驱动方法
0. Python核心编程(第二版)
0. Web性能权威指南
0. 大型网站技术架构
0. 测试架构师修炼之道：从测试工程师到测试架构师
0. MacTalk：人生元编程
0. 正则指引
0. 网站分析实战
0. 架构之美
0. 安全之美
0. web容量规划的艺术
0. 设计模式之禅
0. 利用python进行数据分析
0. 构建高可用linux服务器
0. 算法技术手册

微信读书：

0. "我"：移动互联网创业的未来
0. 创新的洞见
0. 梦里花落知多少 三毛传
0. 小米模式：互联网经济下的超速崛起之道
0. 周鸿炜：人生就是不停的战斗
0. 长尾理论
0. 货币的祸害
0. 世界太大还是遇见你：林徽因传
0. 刻意练习：如何从新手到大师
0. 季羡林私人史
0. 给大家看的中国通史
0. 季羡林谈人生
0. 移动时代：我们如何生存
0. 看见
0. 告诉你一个卓别林的故事
0. 读懂日本：菊与刀
0. 货币战争
0. 从零开始读懂金融学
0. 互联网时代项目管理术
0. 超级IP：互联网时代的跨界营销
0. 地狱
0. 从零开始读懂经济学
0. 国富论
0. 全球通史
0. 习惯的力量
0. 追随你的心
0. 十亿美金的教训
0. 互联网商业思维
0. 产品经理修炼之道
0. 我心向阳，无谓悲伤
0. 银带
0. 你一定爱读的极简金融史
0. 新经济 新规则
0. 心理学的诡计大全集
0. 互联网思维赢利模式
0. 一本书读懂大数据
0. 世界是部金融史
0. 网站数据分析
0. 移动的帝国：日本移动互联网兴衰启示录

![jay](http://o84t5lcxv.bkt.clouddn.com/7396f49ea45917e737021bfe17193ba7.png)
