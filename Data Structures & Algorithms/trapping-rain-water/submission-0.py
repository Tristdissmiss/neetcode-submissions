class Solution:
    def trap(self, height: List[int]) -> int: 
        
        if not height: 
            return 0

        left = 0
        right = len(height)-1 
        res = 0

        max_val_left = height[left]
        max_val_right = height[right]

        while left < right:
            if max_val_left < max_val_right:
                left+=1 
                max_val_left = max(max_val_left, height[left])
                res += max_val_left - height[left]
            else: 
                right -= 1
                max_val_right = max(max_val_right, height[right])
                res += max_val_right - height[right]

        return res

        