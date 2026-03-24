def subtract_two_numbers(a, b):
    """计算两个数的差 (a - b)"""
    return a - b

def subtract_multiple_numbers(*args):
    """计算多个数的连续差 (从左到右依次相减)"""
    if not args:
        return 0
    total = args[0]
    for num in args[1:]:
        total -= num
    return total

def interactive_subtract():
    """交互式减法计算器"""
    print("交互式减法计算器 (输入 'quit' 退出)")
    while True:
        try:
            user_input = input("请输入第一个数字 (被减数): ")
            if user_input.lower() == 'quit':
                break
            a = float(user_input)
            
            user_input = input("请输入第二个数字 (减数): ")
            if user_input.lower() == 'quit':
                break
            b = float(user_input)
            
            result = subtract_two_numbers(a, b)
            print(f"{a} - {b} = {result}")
        except ValueError:
            print("请输入有效的数字！")
        except KeyboardInterrupt:
            print("\n程序已退出")
            break

# 演示代码
if __name__ == "__main__":
    # 两个数相减
    result1 = subtract_two_numbers(10, 3)
    print(f"10 - 3 = {result1}")
    
    # 多个数连续相减
    result2 = subtract_multiple_numbers(100, 20, 10, 5)
    print(f"100 - 20 - 10 - 5 = {result2}")
    
    # 如需启用交互模式，请取消下面一行的注释
    # interactive_subtract()
