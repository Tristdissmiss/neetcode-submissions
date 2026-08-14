class Solution:
    def isValid(self, s: str) -> bool:
        # you cant do two pointer because of some test cases it wouldnt comppletely pass so we need to use a stack 
        # you can use have to use a stack and a map for this problem 

#map 
        close_to_open = {")": "(", "}": "{", "]": "["} 

#stack
        stack = []

        for char in s: 
            if char in close_to_open: 
        #stack cant be empty and top of it has to match with 
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
