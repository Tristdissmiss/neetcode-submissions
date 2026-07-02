class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    #in  sliding window get use to the fact 
    #you need to start in beginning of the string 
    # A window is valid when the total length of current window - count of the most frequent char < = k

    #keep track of char freq in the window 
        count = {}
        left  = 0 
        max_length = 0 
        max_freq = 0 

        for right in range(len(s)):
        #adding a char to the map 
            count[s[right]] = 1 + count.get(s[right], 0)

        #updating the max freq in out current window 
            max_freq = max(max_freq, count[s[right]])

            len_window = right - left + 1

            if len_window - max_freq > k:
                count[s[left]] -= 1 
                left += 1 

            max_length = max(max_length, right - left + 1)

        return max_length
