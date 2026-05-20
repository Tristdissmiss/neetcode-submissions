class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        #cant have duplicates
        #make the first number an a value 
        #make b as the second last 
        #make c the last element 
        #then move a the a pointer, but thats not good, cuz the array will have duplicates potentially 
        
        #fix that we sort the array 
        #if a was the value previous we skip that number if it pops again 

        #so initialize the value with the first value and use double pointers 
        #sum was greater than zero we move the right pointer to a lower number 
        #sum was greater than zero we move the left pointer 

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums) - 1

            while left < right: 
                current_sum = a + nums[left] + nums[right]
                if current_sum > 0: 
                    right -= 1
                elif current_sum < 0: 
                    left += 1
                else: 
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1 
        return res


        