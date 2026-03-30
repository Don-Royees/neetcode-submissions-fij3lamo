class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for x in range(0,len(nums)):
                if nums[i]+ nums[x] == target and i!=x:
                    return[i,x]