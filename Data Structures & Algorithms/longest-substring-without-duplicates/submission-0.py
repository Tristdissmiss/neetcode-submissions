class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #we can go through through the array
        #have like two pointers 
        #a fast and slow pointer 
        #then we can add those chars to a set 
        #if the pointers see a duplcate in the set then the window gets smaller
        #if not we will just add the current inside the set
        #then return the size 
        
        #creating the set '
        char_set = set()
        left = 0 
        max_length = 0 

        #right to move as the fast pointer 
        for right in range(len(s)):

            #if we see a duplicate, shrink the window from the left 
            while s[right] in char_set: 
                char_set.remove(s[left])
                left += 1
            #adding the char that is unique and putting it into the set 
            char_set.add(s[right])

            #Update the max length, comparison to the window
            max_length = max(max_length, right- left+1) 

        return max_length

