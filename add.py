#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的加法脚本
"""

def add(a, b):
    """返回两个数的和"""
    return a + b

if __name__ == "__main__":
    # 示例：计算两个数的和
    num1 = 5
    num2 = 3
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
    
    # 也可以从用户输入获取数字
    try:
        user_num1 = float(input("请输入第一个数字: "))
        user_num2 = float(input("请输入第二个数字: "))
        user_result = add(user_num1, user_num2)
        print(f"{user_num1} + {user_num2} = {user_result}")
    except ValueError:
        print("请输入有效的数字！")
