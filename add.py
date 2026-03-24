#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 加法脚本
支持多种加法操作模式
"""

def add_two_numbers(a, b):
    """计算两个数的和"""
    return a + b

def add_multiple_numbers(*args):
    """计算多个数的和"""
    return sum(args)

def interactive_add():
    """交互式加法计算器"""
    print("=== Python 加法计算器 ===")
    print("输入 'q' 退出程序")
    
    while True:
        user_input = input("\n请输入两个数字（用空格分隔）: ")
        
        if user_input.lower() == 'q':
            print("感谢使用，再见！")
            break
        
        try:
            numbers = list(map(float, user_input.split()))
            
            if len(numbers) != 2:
                print("错误：请输入恰好两个数字")
                continue
            
            result = add_two_numbers(numbers[0], numbers[1])
            print(f"结果: {numbers[0]} + {numbers[1]} = {result}")
            
        except ValueError:
            print("错误：请输入有效的数字")

def main():
    """主函数 - 演示加法功能"""
    # 示例1: 两个数相加
    num1, num2 = 5, 3
    result = add_two_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")
    
    # 示例2: 多个数相加
    numbers = [1, 2, 3, 4, 5]
    result = add_multiple_numbers(*numbers)
    print(f"{' + '.join(map(str, numbers))} = {result}")
    
    # 示例3: 交互式模式（取消注释以启用）
    # interactive_add()

if __name__ == "__main__":
    main()
