class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        n_list=[]
        for i in range(len(nums)):
            if not i < 1:
                left = left * nums[i-1]
            total = 1    
            for x in range(i+1 , len(nums)):
                total = total * nums[x] 
            n_list.append(total * left)
        return n_list        
