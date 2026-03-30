class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topFrequent = []
        for x in range(k):
            frequency = 0 
            num = 0 
            for i in range(len(nums)):
                if nums.count(nums[i]) > frequency :
                    frequency = nums.count(nums[i])
                    num = nums[i]
                    print(num)
            topFrequent.append(num)
            for i in range(frequency): 
                nums.remove(num)
            print(nums)            
        return topFrequent