class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:   
       from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1. Output list and monotonic deque (stores INDICES, not values)
        res = []
        q = deque()  
        
        l = 0
        
        for r in range(len(nums)):
            # 2. Maintain decreasing order in deque: pop smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Add current index
            q.append(r)
            
            # 3. Remove index from front if it fell out of the left side of the window
            if l > q[0]:
                q.popleft()
            
            # 4. Append max to res once window reaches size k
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1  # Slide left pointer forward
                
        return res

