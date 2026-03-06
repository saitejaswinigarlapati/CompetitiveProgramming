from collections import defaultdict
from math import inf

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d, rgt = defaultdict(int), inf
        
        # Count frequency of each number
        for num in nums:
            d[num] += 1

        # Find smallest number and its frequency
        (lft, lftCnt), keys = min(d.items()), sorted(d)

        # Find smallest number whose frequency is different
        for num, numCnt in d.items():
            if numCnt != lftCnt and num < rgt:
                rgt = num

        # Return result
        return [-1, -1] if rgt == inf else [lft, rgt]


# Example run
nums = [1, 2, 2, 3, 3, 3]

sol = Solution()
result = sol.minDistinctFreqPair(nums)

print("Input:", nums)
print("Output:", result)