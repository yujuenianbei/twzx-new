def multiply_two_numbers(a, b):
    """计算两个数的积"""
    return a * b

def multiply_multiple_numbers(*args):
    """计算多个数的积"""
    if not args:
        return 0
    product = 1
    for num in args:
        product *= num
    return product

def interactive_multiply():
    """交互式乘法计算器"""
    print("交互式乘法计算器 (输入 'quit' 退出)")
    while True:
        try:
            user_input = input("请输入第一个数字: ")
            if user_input.lower() == 'quit':
                break
            a = float(user_input)
            
            user_input = input("请输入第二个数字: ")
            if user_input.lower() == 'quit':
                break
            b = float(user_input)
            
            result = multiply_two_numbers(a, b)
            print(f"{a} * {b} = {result}")
        except ValueError:
            print("请输入有效的数字！")
        except KeyboardInterrupt:
            print("\n程序已退出")
            break

# 演示代码
if __name__ == "__main__":
    # 两个数相乘
    result1 = multiply_two_numbers(6, 7)
    print(f"6 * 7 = {result1}")
    
    # 多个数相乘
    result2 = multiply_multiple_numbers(2, 3, 4, 5)
    print(f"2 * 3 * 4 * 5 = {result2}")
    
    # 如需启用交互模式，请取消下面一行的注释
    # interactive_multiply()
