# 孕育管家IOS UI TEST，基于 Facebook WebDriverAgent 简单demo

来自开源项目: https://github.com/openatx/facebook-wda

1. 启动 WebDriverAgent

    git clone https://github.com/facebook/WebDriverAgent

    处理好xcode验证

    在命令行输入:
    
    > 启动真机
    
    ```
    xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id=baa8e87531d4a7bb7b1947e9c2c70df6762e3a6e -configuration Debug test
    ```
    
    > 启动模拟器
    
    ```
    xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'platform=iOS Simulator,name=iPhone 6' test
    ```
    
2.  修改 login.py 中的路径和端口

3.  运行 login.py