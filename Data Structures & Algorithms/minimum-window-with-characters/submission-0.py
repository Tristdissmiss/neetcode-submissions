
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Basecase: return "" if t is longer than s  
        if len(t) > len(s) or not s or not t: 
            return ""

        # Build frequency map for t 
        count_t = {}
        for char in t: 
            count_t[char] = count_t.get(char, 0) + 1  

        # Creating the frequency table 
        window = {} 
        have = 0 
        need = len(count_t)

        # Storing result pointer [left, right] and min length found 
        res = [-1, -1]
        res_len = float("inf")

        left = 0  

        # Moving the right pointer across string s 
        for right in range(len(s)): 
            char = s[right]
            window[char] = window.get(char, 0) + 1 

            # Check if the current char reaches the required frequency in count_t
            # FIX: Placed INSIDE the for right loop
            if char in count_t and window[char] == count_t[char]:
                have += 1 

            # Shrink the left pointer while window contains all required chars 
            while have == need: 
                if (right - left + 1) < res_len: 
                    res = [left, right]
                    res_len = right - left + 1

                # Remove character at s[left] to shrink the window 
                left_char = s[left]
                window[left_char] -= 1 

                if left_char in count_t and window[left_char] < count_t[left_char]: 
                    have -= 1

                left += 1  # Move left pointer forward

        # Return the substring 
        l, r = res 
        return s[l : r + 1] if res_len != float("inf") else ""