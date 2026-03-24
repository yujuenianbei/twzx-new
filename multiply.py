#!/usr/bin/env python3
"""简单的乘法脚本"""

def multiply(a, b):
    """返回两个数的乘积"""
    return a * b

if __name__ == "__main__":
    # 示例计算
    num1 = 7
    num2 = 6
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
    
    # 用户输入计算
    try:
        user_num1 = float(input("请输入第一个数: "))
        user_num2 = float(input("请输入第二个数: "))
        user_result = multiply(user_num1, user_num2)
        print(f"{user_num1} * {user_num2} = {user_result}")
    except ValueError:
        print("输入无效，请输入数字。")
