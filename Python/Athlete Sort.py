"""
Hacker Rank - > Athlete Sort
You are given a spreadsheet that contains a list of  'N' athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.

"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input("Enter N M ").split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    print(f"Enter {n} lines with {m} elements ")
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
arr.sort(key=lambda x: x[k])
for row in arr:
    print(*row)
