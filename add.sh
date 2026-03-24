#!/bin/bash

# 简单的加法脚本
# 用法: ./add.sh <数字1> <数字2>

# 检查是否提供了两个参数
if [ $# -ne 2 ]; then
    echo "用法: $0 <数字1> <数字2>"
    echo "示例: $0 5 3"
    exit 1
fi

# 获取参数
num1=$1
num2=$2

# 计算和
sum=$((num1 + num2))

# 输出结果
echo "$num1 + $num2 = $sum"
