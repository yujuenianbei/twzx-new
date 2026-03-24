#!/usr/bin/env python3
"""简单的除法脚本"""

import sys

def divide(a, b):
    """执行除法运算"""
    if b == 0:
        raise ValueError("错误：除数不能为零！")
    return a / b

def main():
    if len(sys.argv) != 3:
        print("用法：python3 divide.py <被除数> <除数>")
        print("示例：python3 divide.py 10 2")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("错误：请输入有效的数字！")
        else:
            print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
