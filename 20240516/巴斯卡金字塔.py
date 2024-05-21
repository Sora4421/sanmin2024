# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:56:08 2024

@author: User
"""

def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    n = len(triangle)
    for row in triangle:
        # 計算前面需要打印的空格數量
        spaces = ' ' * (n - len(row))
        # 使用空格將每個數字分開
        row_str = ' '.join(map(str, row))
        # 打印每一行
        print(spaces + row_str)

# 設置行數
n = 5
# 生成巴斯卡三角形
triangle = generate_pascals_triangle(n)
# 打印巴斯卡三角形
print_pascals_triangle(triangle)
