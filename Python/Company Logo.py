"""
Hacker Rank -> Company Logo
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input("Enter string :")
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    sorted_items = sorted(dic.items(), key=lambda item: (-item[1], item[0]))
    for i in range(min(3, len(sorted_items))):
        print(sorted_items[i][0], sorted_items[i][1])
        
"""
Sample Input : aabbbccde
Sample output :
b 3
a 2
c 2
"""