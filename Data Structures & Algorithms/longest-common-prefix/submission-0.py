class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #doing vertical scanning 
        #gonna line up the strings and use first string as the parent to the rest of the strings 

        #edge case fo no strings 
        if not strs: 
            return ""
        
        #the parent or the example word 
        first_word = strs[0]
        #to witness the chars in the string 
        for i in range(len(first_word)):
            char_to_see = first_word[i]
            #checking the other index for the other words 
            for other_word in strs[1:]:
                if i >= len(other_word) or other_word[i] != char_to_see:
                    return first_word[:i]

        return first_word
         
    


        