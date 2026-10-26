class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #o(logn) time
        #o(1) space
        # maybe l and r at the start and end then 
        #use l+r / 2 to find mid then calculate if left/ right is sorted by checking if mid is greateer than l and less than r from there 

        left , right = 0 , len(nums) - 1
        while left <= right :
            mid = (left+right) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid] :
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1

        return -1                          