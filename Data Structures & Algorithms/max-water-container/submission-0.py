class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left = 0 
        right = n-1
        maxArea = 0
        while left < right:
            width = right - left
            temp = min(heights[left],heights[right])
            area = width * temp 
            maxArea = max(area,maxArea)

            if heights[left] < heights[right]:
                left+=1
            
            else:
                right-=1

        return maxArea

        