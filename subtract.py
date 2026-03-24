def subtract(a, b):
    """减法函数"""
    return a - b

if __name__ == "__main__":
    try:
        num1 = float(input("请输入第一个数字（被减数）: "))
        num2 = float(input("请输入第二个数字（减数）: "))
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    except ValueError:
        print("错误：请输入有效的数字")
