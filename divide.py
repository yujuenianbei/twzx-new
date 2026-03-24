#!/usr/bin/env python3
"""
简单的除法脚本
支持两个数相除，并处理除零错误和输入验证
"""

def divide(a, b):
    """执行除法运算"""
    if b == 0:
        raise ValueError("错误：除数不能为零！")
    return a / b

def main():
    print("=== Python 除法计算器 ===")
    
    try:
        # 获取用户输入
        num1 = float(input("请输入被除数: "))
        num2 = float(input("请输入除数: "))
        
        # 执行除法
        result = divide(num1, num2)
        
        # 显示结果
        print(f"\n结果: {num1} ÷ {num2} = {result}")
        
    except ValueError as e:
        print(f"\n{e}")
    except Exception as e:
        print(f"\n发生错误: {e}")

if __name__ == "__main__":
    main()
