#!/usr/bin/env python3
"""
Python 减法脚本
支持命令行参数和交互两种模式
"""

import sys

def subtract(a, b):
    """执行减法运算"""
    return a - b

def main():
    # 如果提供了命令行参数
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = subtract(num1, num2)
            
            # 如果结果是整数，显示为整数格式
            if result.is_integer():
                print(f"{int(num1)} - {int(num2)} = {int(result)}")
            else:
                print(f"{num1} - {num2} = {result}")
        except ValueError:
            print("错误：请输入有效的数字")
            sys.exit(1)
    elif len(sys.argv) == 1:
        # 交互模式
        print("Python 减法计算器")
        print("输入 'q' 退出")
        
        while True:
            try:
                user_input1 = input("\n请输入被减数: ")
                if user_input1.lower() == 'q':
                    print("再见！")
                    break
                    
                user_input2 = input("请输入减数: ")
                if user_input2.lower() == 'q':
                    print("再见！")
                    break
                
                num1 = float(user_input1)
                num2 = float(user_input2)
                
                result = subtract(num1, num2)
                
                # 如果结果是整数，显示为整数格式
                if result.is_integer():
                    print(f"结果: {int(num1)} - {int(num2)} = {int(result)}")
                else:
                    print(f"结果: {num1} - {num2} = {result}")
                    
            except ValueError:
                print("错误：请输入有效的数字")
            except KeyboardInterrupt:
                print("\n再见！")
                break
    else:
        print("用法:")
        print("  命令行模式: python subtract.py <被减数> <减数>")
        print("  交互模式:   python subtract.py")
        sys.exit(1)

if __name__ == "__main__":
    main()
