#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def subtract(a, b):
    """返回两个数的差"""
    return a - b

if __name__ == "__main__":
    # 示例计算
    num1 = 10
    num2 = 4
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
    
    # 用户输入计算
    try:
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        result = subtract(a, b)
        print(f"{a} - {b} = {result}")
    except ValueError:
        print("输入无效，请输入数字。")
