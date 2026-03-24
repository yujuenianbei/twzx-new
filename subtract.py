#!/usr/bin/env python3
"""减法脚本：计算两个数字的差"""

import sys

def subtract(a, b):
    return a - b

def main():
    if len(sys.argv) != 3:
        print("用法: python3 subtract.py <数字1> <数字2>")
        print("示例: python3 subtract.py 10 3")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("错误: 请输入有效的数字")
        sys.exit(1)
    
    result = subtract(num1, num2)
    
    # 如果结果是整数，去掉小数部分
    if result == int(result):
        print(int(result))
    else:
        print(result)

if __name__ == "__main__":
    main()
