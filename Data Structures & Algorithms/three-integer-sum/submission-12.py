class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l , r = 0 , len(nums) - 1
        nlist = []
        nums.sort()
        for i , x in enumerate(nums):
            l=i+1
            r=len(nums) -1
            while l<r:
                if nums[l]+nums[r]+x < 0:
                    l=l+1
                elif nums[l]+nums[r]+x > 0:
                    r=r-1
                elif nums[l]+nums[r]+x == 0:
                    item = [nums[l],nums[r],x]
                    if item not in nlist:
                        nlist.append([nums[l],nums[r],x])
                    l+=1
        return nlist                    
                    
                    