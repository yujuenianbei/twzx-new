#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
乘法脚本 - 计算两个数的乘积
"""

def multiply(a, b):
    """返回两个数的乘积"""
    return a * b

def main():
    print("=== 乘法计算器 ===")
    
    # 获取用户输入
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        
        # 计算乘积
        result = multiply(num1, num2)
        
        # 显示结果
        print(f"\n{num1} × {num2} = {result}")
        
    except ValueError:
        print("错误：请输入有效的数字！")

if __name__ == "__main__":
    main()
