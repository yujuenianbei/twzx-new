def divide(a, b):
    if b == 0:
        return "错误：除数不能为零"
    return a / b

# 示例使用
num1 = 10
num2 = 2
result = divide(num1, num2)
print(f"{num1} / {num2} = {result}")

# 测试除数为零的情况
result_zero = divide(5, 0)
print(f"5 / 0 = {result_zero}")
