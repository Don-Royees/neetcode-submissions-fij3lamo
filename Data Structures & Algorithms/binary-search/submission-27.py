class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right :
            midpoint = (right + left) // 2 
            print(nums[midpoint])
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] < target:
                left = midpoint + 1
            if nums[midpoint] > target:
                right = midpoint - 1
        return -1             
            