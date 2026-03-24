#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python 乘法脚本
支持两个数相乘，包含输入验证和错误处理
"""

def multiply():
    print("=== Python 乘法计算器 ===")
    
    try:
        # 获取用户输入
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        
        # 计算乘积
        result = num1 * num2
        
        # 显示结果
        print(f"\n结果: {num1} × {num2} = {result}")
        
    except ValueError:
        print("\n错误：请输入有效的数字！")
    except KeyboardInterrupt:
        print("\n\n操作已取消。")
    except Exception as e:
        print(f"\n发生未知错误: {e}")

if __name__ == "__main__":
    multiply()
