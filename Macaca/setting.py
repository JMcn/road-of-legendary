#coding=utf-8
import os

# 真机参数
desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '9.3.5',
    'deviceName': 'iPhone',
    'autoAcceptAlerts': 'true',
    'udid': 'baa8e87531d4a7bb7b1947e9c2c70df6762e3a6e',
    'bundleId': 'com.gzmama.mama.PregnancyHelper',
    'reuse': '3',
}

# 模拟器参数
desired_caps_sim = {
    'platformName': 'iOS',
    'platformVersion': '10.1',
    'deviceName': 'iPhone 6s',
    'autoAcceptAlerts': 'true',
    'app': os.path.dirname(os.path.abspath(__file__)) + '/pregnancy_ios_debug_simulator_4.zip',
    'bundleId': 'com.gzmama.mama.PregnancyHelper',
    'reuse': '1',
}

server_url = {
    'hostname': '127.0.0.1',
    'port': 3456
}