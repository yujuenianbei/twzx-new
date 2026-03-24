#!/usr/bin/env python3
"""简单的加法脚本：接收两个数字，输出它们的和。"""

def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        try:
            x = float(sys.argv[1])
            y = float(sys.argv[2])
            result = add(x, y)
            # 如果是整数则显示为整数
            if result.is_integer():
                print(int(result))
            else:
                print(result)
        except ValueError:
            print("错误：请输入有效的数字。")
            sys.exit(1)
    else:
        print(f"用法: python {sys.argv[0]} <数字1> <数字2>")
        print("示例: python add.py 3 5")
