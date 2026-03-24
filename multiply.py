#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
乘法脚本 - 支持多种乘法运算功能
"""

def multiply(a, b):
    """返回两个数的乘积"""
    return a * b

def multiplication_table(n):
    """打印 n 的乘法表（1 到 9）"""
    print(f"=== {n} 的乘法表 ===")
    for i in range(1, 10):
        print(f"{n} × {i} = {multiply(n, i)}")
    print()

def full_multiplication_table():
    """打印完整的 9×9 乘法表"""
    print("=== 9×9 乘法表 ===")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}×{i}={multiply(j, i):2}", end="  ")
        print()
    print()

def main():
    print("欢迎使用乘法脚本！")
    print("=" * 40)
    
    # 示例：基本乘法
    a, b = 6, 7
    result = multiply(a, b)
    print(f"{a} × {b} = {result}")
    print()
    
    # 示例：单个数字的乘法表
    multiplication_table(6)
    
    # 示例：完整 9×9 乘法表
    full_multiplication_table()
    
    # 交互式输入
    try:
        user_input = input("请输入两个数字进行乘法运算（格式：a b），或直接回车跳过：").strip()
        if user_input:
            parts = user_input.split()
            if len(parts) == 2:
                x, y = float(parts[0]), float(parts[1])
                print(f"{x} × {y} = {multiply(x, y)}")
            else:
                print("输入格式不正确，请使用：a b")
    except ValueError:
        print("请输入有效的数字！")
    except KeyboardInterrupt:
        print("\n程序已中断。")

if __name__ == "__main__":
    main()
