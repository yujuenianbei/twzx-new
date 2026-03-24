#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的加法脚本

功能：计算两个数字的和，支持命令行参数和交互式输入两种方式。

使用方法：
    1. 命令行模式: python add.py <数字1> <数字2>
    2. 交互模式: python add.py
    3. 查看帮助: python add.py --help

示例：
    $ python add.py 5 3
    5 + 3 = 8

    $ python add.py 2.5 4.5
    2.5 + 4.5 = 7.0
"""

import sys
import argparse
from typing import Union


def format_number(num: float) -> Union[int, float]:
    """
    格式化数字：如果是整数则返回 int 类型，否则保留原样。
    
    Args:
        num: 输入的数字
        
    Returns:
        如果小数部分为 0 则返回整数，否则返回浮点数
    """
    return int(num) if num.is_integer() else num


def add(a: float, b: float) -> float:
    """
    计算两个数的和。
    
    Args:
        a: 第一个加数
        b: 第二个加数
        
    Returns:
        两数之和
    """
    return a + b


def parse_arguments() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description='简单的加法计算器 - 计算两个数字的和',
        epilog='示例: python add.py 10 20'
    )
    parser.add_argument(
        'numbers',
        nargs='*',
        type=float,
        help='要相加的两个数字'
    )
    return parser.parse_args()


def get_interactive_input() -> tuple[float, float]:
    """
    通过交互式方式获取用户输入。
    
    Returns:
        包含两个浮点数的元组
        
    Raises:
        ValueError: 当输入不是有效数字时
        KeyboardInterrupt: 当用户中断输入时
    """
    print("=== 简单加法计算器 ===")
    
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        return num1, num2
    except ValueError:
        raise ValueError("错误：请输入有效的数字")


def main() -> None:
    """主函数：处理命令行参数或交互式输入并执行加法运算。"""
    args = parse_arguments()
    
    # 命令行模式
    if len(args.numbers) == 2:
        num1, num2 = args.numbers
    elif len(args.numbers) == 0:
        # 交互式模式
        try:
            num1, num2 = get_interactive_input()
        except (ValueError, KeyboardInterrupt) as e:
            if isinstance(e, ValueError):
                print(e)
            else:
                print("\n操作已取消")
            sys.exit(1)
    else:
        print(f"错误：需要提供 0 个或 2 个数字，当前提供了 {len(args.numbers)} 个")
        print("使用方法: python add.py [数字1] [数字2]")
        print("或者运行: python add.py --help")
        sys.exit(1)
    
    # 执行加法并输出结果
    result = add(num1, num2)
    
    # 格式化输出（整数不显示小数点）
    num1_fmt = format_number(num1)
    num2_fmt = format_number(num2)
    result_fmt = format_number(result)
    
    print(f"{num1_fmt} + {num2_fmt} = {result_fmt}")


if __name__ == "__main__":
    main()
