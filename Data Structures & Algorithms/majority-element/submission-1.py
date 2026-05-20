class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        #gives frequency type question 
        #im thinking hash map 
        #have a counter val 
        #if the you see the key in the arr add a val 
        #if its new add 
        #if there is a counter val > len(nums)//2 
        #return key  

        counts = {} 
        majority_mid = len(nums)//2 

        for num in nums: 
            if num in counts:
                counts[num]+=1 
            else:
                counts[num] = 1 
        
            if counts[num] > majority_mid: 
                return num
        