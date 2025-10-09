#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pika Sense 示例代码
演示如何查询 pika Sense 固件版本信息
"""

import time
from pika import sense

def main():
    # 创建 Sense 对象并连接
    print("正在连接 Pika Sense 设备...")
    my_sense = sense('/dev/ttyUSB0')  # 请根据实际情况修改串口路径,默认参数为：/dev/ttyUSB0
    
    if not my_sense.connect():
        print("连接 Pika Sense 设备失败，请检查设备连接和串口路径")
        return
    
    print("成功连接到 Pika Sense 设备")
    print("获取版本信息...")
    # 每0.1秒发送一次get_version()命令,循环5次
    for _ in range(5):
        my_sense.get_version()
        # 休眠0.1秒等待数据返回
        time.sleep(0.1)



if __name__ == "__main__":
    main()