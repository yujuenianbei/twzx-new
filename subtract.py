#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的减法脚本
使用方法：python subtract.py <数字1> <数字2>
"""

import sys

def subtract(a, b):
    """执行减法运算"""
    return a - b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法：python subtract.py <数字1> <数字2>")
        print("示例：python subtract.py 10 3")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    except ValueError:
        print("错误：请输入有效的数字")
        sys.exit(1)
