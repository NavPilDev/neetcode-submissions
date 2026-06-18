class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if (i == j):
                    continue
                res[j] *= n
        
        # At each res[i], the product of every element of nums[] except
        # nums[i] is stored.
        return res