# 1. Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i
        
        return [0,0]

print(Solution().twoSum([2,7,11,15], 9))  # [0,1]
print(Solution().twoSum([3,2,4], 6))  # [1,2]
print(Solution().twoSum([3,3], 6))  # [0,1]
