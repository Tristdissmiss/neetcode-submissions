class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        #we are going to have a result hashmap instead 
        #it will give the value as the key and value as the index 
        #same idea with subtracting th target to see if in the array we can find the 
        res = {}

        for i,n in enumerate(nums): 
            diff = target - n
            if diff in res: 
                return[res[diff], i]
            res[n] = i 
        return 
        


        

        