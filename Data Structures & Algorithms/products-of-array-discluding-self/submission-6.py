class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time && O(1) space solution

        prev = 1
        res = [1] * len(nums)
        # prefix step
        for i in range(len(nums)):
            res[i] = prev
            prev *= nums[i] 

        print(res)
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        '''
        ##################################################
        # O(n) Solution
        # Create prefix and suffix arrays
        # Prefix(left-to-right) will contain the products of the current element of num and previous element
        # of prefix at the current element of prefix
        # Suffix(right-to-left) will contain the products of the current element of num and previous element
        # of suffix at the current element of suffix
        res, prefix, suffix = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        count = 0;
        # Previous Element
        prev = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                prefix[i] = num
                continue
            prefix[i] = num * prev
            prev = prefix[i]
        prev = 0
       
        for i, num in reversed(list(enumerate(nums))):
            if i == len(nums) - 1:
                suffix[i] = num
                prev = num
                continue
            suffix[i] = num * prev
            prev = suffix[i]
        # To get product except self at ever element of res
        # we have to calculate the product using the element at the index before in the prefix
        # and the element in the index after in the suffix.
        for i in range(len(res)):
            res[i] = (prefix[i-1] if i - 1 >= 0  else 1)* (suffix[i+1] if i != len(res) - 1  else 1)
        ###########################################
        # O(n^2) Solution
        # res = [1] * len(nums)
        # for i, n in enumerate(nums):
        #     for j, m in enumerate(nums):
        #         if (i == j):
        #             continue
        #         res[j] *= n
        
        # At each res[i], the product of every element of nums[] except
        # nums[i] is stored.
        '''
        return res