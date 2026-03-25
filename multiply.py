#!/usr/bin/env python3
"""
简单的乘法脚本
支持两种模式：
1. 命令行参数模式：python multiply.py 5 3
2. 交互模式：直接运行 python multiply.py，然后输入两个数字
"""

import sys

def multiply(a, b):
    """返回两个数的乘积"""
    return a * b

def main():
    if len(sys.argv) == 3:
        # 命令行参数模式
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = multiply(num1, num2)
            print(f"{num1} × {num2} = {result}")
        except ValueError:
            print("错误：请输入有效的数字")
            sys.exit(1)
    else:
        # 交互模式
        print("=== 乘法计算器 ===")
        try:
            num1 = float(input("请输入第一个数字: "))
            num2 = float(input("请输入第二个数字: "))
            result = multiply(num1, num2)
            print(f"\n{num1} × {num2} = {result}")
        except ValueError:
            print("错误：请输入有效的数字")
            sys.exit(1)
        except EOFError:
            print("\n操作已取消")
            sys.exit(0)

if __name__ == "__main__":
    main()
