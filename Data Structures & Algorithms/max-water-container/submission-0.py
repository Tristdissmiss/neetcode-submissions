class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        #we care about max area 
        #if the smaller pointer is less than the other pointer 
        #move it  
        #if they have the same height move one of the pointers 
        result = 0 
        left = 0 
        right = len(heights) - 1 

        while left < right: 
            #area of rectangle 
            area = (right - left) * min(heights[left], heights[right])  
            result = max(result, area) 

            if heights[left] < heights[right]:
                left += 1 
            
            else: 
                right -= 1
            
        return result
            

        