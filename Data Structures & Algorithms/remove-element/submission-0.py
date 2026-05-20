class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #one pointer 
        k = 0 
        #interate other pointer 
        for i in range(len(nums)): 
            #if nums doesnt equal val
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k