class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        high = 0 
        if not nums:
            return 0
        for i in nums:
            if i - 1 not in set_nums:
                curr = 1
                while i + 1 in set_nums:
                    curr = curr + 1
                    i = i + 1
                high = max(curr , high)
        return high           

            
