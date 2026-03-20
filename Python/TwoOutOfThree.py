from typing import List, Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = Counter()
        for nums in nums1, nums2, nums3: freq.update(set(nums))
        return [k for k, v in freq.items() if v >= 2]
s=Solution()

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]

print(s.twoOutOfThree(nums1,nums2,nums3))