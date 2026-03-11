from typing import List
class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player = 0
        scores = [0, 0]
        for game, points in enumerate(nums, 1):
            player ^= (points % 2) ^ (game % 6 == 0)
            scores[player] += points

        return scores[0] - scores[1]
    
s=Solution()
nums = [1,2,3]

print(s.scoreDifference(nums))