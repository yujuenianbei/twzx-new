def divide(a, b):
    if b == 0:
        return "错误：除数不能为零"
    return a / b

if __name__ == "__main__":
    try:
        num1 = float(input("请输入被除数: "))
        num2 = float(input("请输入除数: "))
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    except ValueError:
        print("错误：请输入有效的数字")
