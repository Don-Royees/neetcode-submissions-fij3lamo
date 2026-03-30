class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_list=[]
        for i in nums:
            if i in dup_list:
                return True
            else:
                dup_list.append(i)
        return False            