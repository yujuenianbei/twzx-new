#!/usr/bin/env python3
"""简单的除法脚本"""

def divide(a, b):
    """返回两个数的商"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

if __name__ == "__main__":
    # 示例计算
    num1, num2 = 20, 4
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
    
    # 用户输入计算
    try:
        user_num1 = float(input("\n请输入被除数: "))
        user_num2 = float(input("请输入除数: "))
        user_result = divide(user_num1, user_num2)
        print(f"{user_num1} / {user_num2} = {user_result}")
    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
