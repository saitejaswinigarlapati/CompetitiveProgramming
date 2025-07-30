# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.


from typing import List
from collections import defaultdict

def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 1

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] += 1

    return count

ls = [1, 2, 3]
k = 3
print(f"Total number of continuous subarrays whose sum equals to {k}: {subarraySum(ls, k)}")
