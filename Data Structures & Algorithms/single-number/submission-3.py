class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found = set()
        for i in nums:
            if i in found:
                found.remove(i)
            else:
                found.add(i)
        for i in found:
            return i            