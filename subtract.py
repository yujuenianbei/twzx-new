#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def subtract(a, b):
    """返回两个数的差"""
    return a - b

if __name__ == "__main__":
    # 示例用法
    num1 = 10
    num2 = 4
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
    
    # 用户输入
    try:
        user_num1 = float(input("\n请输入第一个数字: "))
        user_num2 = float(input("请输入第二个数字: "))
        user_result = subtract(user_num1, user_num2)
        print(f"{user_num1} - {user_num2} = {user_result}")
    except ValueError:
        print("输入无效，请输入数字。")
