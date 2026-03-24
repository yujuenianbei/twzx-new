#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单的加法脚本
支持多种输入方式和批量计算
"""

import sys
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """返回两个数的和
    
    Args:
        a: 第一个数字
        b: 第二个数字
    
    Returns:
        两数之和
    """
    return a + b


def get_number(prompt: str) -> Union[int, float]:
    """获取用户输入的数字
    
    Args:
        prompt: 提示信息
    
    Returns:
        用户输入的数字
    
    Raises:
        ValueError: 当输入不是有效数字时
    """
    while True:
        try:
            user_input = input(prompt)
            # 尝试转换为整数，如果不是整数则转换为浮点数
            if '.' in user_input:
                return float(user_input)
            return int(user_input)
        except ValueError:
            print("❌ 输入无效，请输入一个数字！")
        except KeyboardInterrupt:
            print("\n操作已取消")
            sys.exit(0)


def main():
    """主函数"""
    print("=" * 40)
    print("🔢 简单加法计算器")
    print("=" * 40)
    
    # 示例计算
    print("\n📝 示例计算:")
    num1, num2 = 5, 3
    result = add(num1, num2)
    print(f"   {num1} + {num2} = {result}")
    
    # 支持命令行参数（优先模式）
    if len(sys.argv) == 3:
        print("\n💻 命令行模式:")
        try:
            arg1 = float(sys.argv[1])
            arg2 = float(sys.argv[2])
            arg_result = add(arg1, arg2)
            print(f"   {arg1} + {arg2} = {arg_result}")
            return  # 命令行模式下不进入交互
        except ValueError:
            print("   ❌ 命令行参数必须是数字")
            return
    
    # 交互式计算
    print("\n✏️  交互式计算:")
    user_num1 = get_number("请输入第一个数字: ")
    user_num2 = get_number("请输入第二个数字: ")
    user_result = add(user_num1, user_num2)
    print(f"\n✅ 结果: {user_num1} + {user_num2} = {user_result}")


if __name__ == "__main__":
    main()
