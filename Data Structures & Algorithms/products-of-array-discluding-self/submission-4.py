class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) Solution
        res = [1] * len(nums)
        count = 0;
        prefix = [1] * len(nums)
        prev = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                prefix[i] = num
                continue
            prefix[i] = num * prev
            prev = prefix[i]
        prev = 0
        suffix = [1] * len(nums)
        for i, num in reversed(list(enumerate(nums))):
            if i == len(nums) - 1:
                suffix[i] = num
                prev = num
                continue
            suffix[i] = num * prev
            prev = suffix[i]
        for i in range(len(res)):
            res[i] = (prefix[i-1] if i - 1 >= 0  else 1)* (suffix[i+1] if i != len(res) - 1  else 1)
        # O(n^2) Solution
        # res = [1] * len(nums)
        # for i, n in enumerate(nums):
        #     for j, m in enumerate(nums):
        #         if (i == j):
        #             continue
        #         res[j] *= n
        
        # At each res[i], the product of every element of nums[] except
        # nums[i] is stored.
        return res