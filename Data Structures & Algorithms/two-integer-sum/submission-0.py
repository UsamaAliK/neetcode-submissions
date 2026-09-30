class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in num:
                return [num[comp],i]
            else:
                num[nums[i]]=i
            