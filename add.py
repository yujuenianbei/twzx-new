#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python加法脚本
支持两种模式：
1. 命令行参数模式：python add.py 数字1 数字2
2. 交互模式：直接运行python add.py，然后输入两个数字
"""

import sys


def add_numbers(a, b):
    """返回两个数的和"""
    return a + b


def main():
    # 如果提供了命令行参数
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = add_numbers(num1, num2)
            print(f"{num1} + {num2} = {result}")
        except ValueError:
            print("错误：请提供有效的数字作为参数")
            print("用法：python add.py 数字1 数字2")
            sys.exit(1)
    else:
        # 交互模式
        print("=== Python加法计算器 ===")
        print("请输入两个数字进行相加（输入'q'退出）\n")
        
        while True:
            try:
                # 获取第一个数字
                input1 = input("请输入第一个数字: ")
                if input1.lower() == 'q':
                    print("再见！")
                    break
                num1 = float(input1)
                
                # 获取第二个数字
                input2 = input("请输入第二个数字: ")
                if input2.lower() == 'q':
                    print("再见！")
                    break
                num2 = float(input2)
                
                # 计算并显示结果
                result = add_numbers(num1, num2)
                print(f"结果: {num1} + {num2} = {result}\n")
                
            except ValueError:
                print("错误：请输入有效的数字！\n")
            except KeyboardInterrupt:
                print("\n\n再见！")
                break


if __name__ == "__main__":
    main()
