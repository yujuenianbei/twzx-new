#!/usr/bin/env python3
"""一个简单的减法脚本"""

def subtract(a, b):
    """返回两个数的差"""
    return a - b

if __name__ == "__main__":
    # 示例：计算 10 - 3
    num1 = 10
    num2 = 3
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
