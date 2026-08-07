class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0 
        while count in nums:
            count = count + 1 
        return count     
