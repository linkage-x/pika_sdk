#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pika Gripper 示例代码
演示如何查询 pika Gripper 固件版本信息
"""

import time
# 从 pika.gripper 模块导入 Gripper 类
from pika.gripper import Gripper 

def main():
    # 创建 Gripper 对象并连接
    print("正在连接 Pika Gripper 设备...")
    # 使用 Gripper 类进行实例化
    my_gripper = Gripper("/dev/ttyUSB0")  # 请根据实际情况修改串口路径,默认参数为：/dev/ttyUSB0
    
    if not my_gripper.connect():
        print("连接 Pika Gripper 设备失败，请检查设备连接和串口路径")
        return
    
    print("成功连接到 Pika gripper 设备")
    print("获取版本信息...")
    
    # 每0.1秒发送一次get_version()命令,循环5次
    for _ in range(5):
        my_gripper.get_version()
        # 休眠0.1秒等待数据返回
        time.sleep(0.1)


if __name__ == "__main__":
    main()
