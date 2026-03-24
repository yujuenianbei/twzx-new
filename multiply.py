#!/usr/bin/env python3
"""
简单的乘法脚本
支持命令行参数和交互式输入两种方式
可处理整数和小数乘法
包含错误处理
"""

import argparse
import sys
from typing import List, Optional


def parse_arguments() -> Optional[List[float]]:
    """
    解析命令行参数
    
    Returns:
        List[float]: 数字列表，如果未提供参数则返回 None
    """
    parser = argparse.ArgumentParser(
        description='简单的乘法脚本 - 计算两个或多个数字的乘积',
        epilog='示例:\n  python multiply.py 2 3 4\n  python multiply.py 2.5 4',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'numbers',
        nargs='*',
        type=float,
        help='要相乘的数字（可以是整数或小数）'
    )
    
    args = parser.parse_args()
    
    if args.numbers:
        return args.numbers
    return None


def get_interactive_input() -> List[float]:
    """
    从用户交互获取输入
    
    Returns:
        List[float]: 用户输入的数字列表
    """
    print("=== 乘法计算器 ===")
    print("请输入要相乘的数字（用空格分隔），或按 Ctrl+C 退出")
    
    try:
        user_input = input("输入数字: ").strip()
        if not user_input:
            print("错误：未输入任何数字")
            sys.exit(1)
            
        numbers = [float(x) for x in user_input.split()]
        
        if len(numbers) < 2:
            print("错误：请至少输入两个数字")
            sys.exit(1)
            
        return numbers
        
    except ValueError:
        print("错误：请输入有效的数字")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n操作已取消")
        sys.exit(0)


def format_number(num: float) -> str:
    """
    格式化数字显示
    如果是整数则不显示小数点
    
    Args:
        num: 要格式化的数字
        
    Returns:
        str: 格式化后的数字字符串
    """
    if num.is_integer():
        return str(int(num))
    return str(num)


def calculate_product(numbers: List[float]) -> float:
    """
    计算数字列表的乘积
    
    Args:
        numbers: 数字列表
        
    Returns:
        float: 所有数字的乘积
    """
    product = 1.0
    for num in numbers:
        product *= num
    return product


def display_result(numbers: List[float], product: float) -> None:
    """
    显示计算结果
    
    Args:
        numbers: 输入的数字列表
        product: 计算得到的乘积
    """
    formatted_numbers = [format_number(num) for num in numbers]
    expression = " × ".join(formatted_numbers)
    formatted_product = format_number(product)
    
    print(f"{expression} = {formatted_product}")


def main() -> None:
    """主函数"""
    # 尝试从命令行获取参数
    numbers = parse_arguments()
    
    # 如果没有命令行参数，使用交互式输入
    if numbers is None:
        numbers = get_interactive_input()
    
    if len(numbers) < 2:
        print("错误：请提供至少两个数字进行乘法运算")
        sys.exit(1)
    
    # 计算乘积
    product = calculate_product(numbers)
    
    # 显示结果
    display_result(numbers, product)


if __name__ == "__main__":
    main()
