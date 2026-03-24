#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
乘法脚本 - 计算两个数的乘积
"""

def multiply(a, b):
    """返回两个数的乘积"""
    return a * b

if __name__ == "__main__":
    # 示例：计算两个数的乘积
    num1 = float(input("请输入第一个数: "))
    num2 = float(input("请输入第二个数: "))
    
    result = multiply(num1, num2)
    
    print(f"{num1} × {num2} = {result}")
