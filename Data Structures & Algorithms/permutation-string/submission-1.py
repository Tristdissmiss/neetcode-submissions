class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 

        #in sliding window we check 
        #we can make s1 a map to count frequency of word one
        #then we have a map as like a checker 
        #going through the length of map for s1
        #if it has the same amount of chars as the set then that checks the first part if not move over by one character 
        #if the index or position of the chars are like set just flipped around it checks out 
        #then return true 

       
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2: 
            return False
        
        s1_counts = [0] * 26 
        s2_counts = [0] * 26 
        
        #build up the counts of s1 
        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1# the ord is getting the ascii value of the lowercase letter in the index 
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
            return True 

        #moving the sliding window 
        for i in range(n1,n2): 
            s2_counts[ord(s2[i]) - 97] += 1
            #in the counts its making it take out the previous char in the 
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1
            
            #check again  
            if s1_counts == s2_counts: 
                return True 
        
        return False








        