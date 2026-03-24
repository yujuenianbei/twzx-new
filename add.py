#!/usr/bin/env python3
"""简单的加法脚本"""

def add(a, b):
    """返回两个数的和"""
    return a + b

if __name__ == "__main__":
    # 示例：计算 5 + 3
    num1 = 5
    num2 = 3
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
