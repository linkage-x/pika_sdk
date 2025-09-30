#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pika Sense 示例代码
演示如何使用对 Sense 的灯光以及振动马达进行控制
"""

import time
import numpy as np
from pika import sense

def main():
    # 创建 Sense 对象并连接
    print("正在连接 Pika Sense 设备...")
    my_sense = sense('/dev/ttyUSB0')  # 请根据实际情况修改串口路径,默认参数为：/dev/ttyUSB0
    
    if not my_sense.connect():
        print("连接 Pika Sense 设备失败，请检查设备连接和串口路径")
        return
    
    print("成功连接到 Pika Sense 设备")
    
    print("正在执行亮灯操作...")
    print("白灯亮2秒...")
    my_sense.light_ctrl(0)
    time.sleep(2)
    
    print("红灯亮2秒...")
    my_sense.light_ctrl(1)
    time.sleep(2)
    
    print("绿灯亮2秒...")
    my_sense.light_ctrl(2)
    time.sleep(2)
    
    print("蓝灯亮2秒...")
    my_sense.light_ctrl(3)
    time.sleep(2)
    
    print("黄灯亮2秒...")
    my_sense.light_ctrl(4)
    time.sleep(2)
    
    print("正在执行振动马达操作...")
    print("振动2秒...")
    my_sense.vibrate_ctrl(1)
    time.sleep(2)
    print("关闭振动马达...")
    my_sense.vibrate_ctrl(0)


if __name__ == "__main__":
    main()