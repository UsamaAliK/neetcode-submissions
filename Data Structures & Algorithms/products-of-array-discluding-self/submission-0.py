class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n

        prefix = 1

        # Products to the left
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Products to the right
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output