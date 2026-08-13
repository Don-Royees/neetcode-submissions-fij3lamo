class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_size = 0
        l,r = 0 , len(heights) - 1 
        while l<r:
            size = min(heights[l],heights[r]) * (r-l)
            max_size = max(size , max_size)
            if heights[l] <= heights[r]:
                l = l + 1 
            else:
                r = r -1 
        return max_size
