#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的加法脚本
使用方法：
    python add.py <数字1> <数字2>
    或者运行后按提示输入两个数字
"""

import sys

def add(a, b):
    """返回两个数的和"""
    return a + b

def main():
    # 如果提供了命令行参数
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        except ValueError:
            print("错误：请输入有效的数字")
            sys.exit(1)
    else:
        # 交互式输入
        print("=== 简单加法计算器 ===")
        try:
            num1 = float(input("请输入第一个数字: "))
            num2 = float(input("请输入第二个数字: "))
            result = add(num1, num2)
            print(f"\n结果: {num1} + {num2} = {result}")
        except ValueError:
            print("错误：请输入有效的数字")
            sys.exit(1)

if __name__ == "__main__":
    main()
