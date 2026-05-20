class Solution: 

    #read in string 
    #get the length of string 
    #put the length of string with a #(delimiter)
    #theyre put in the front of the string
    #

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += str(len(s)) + "#" + s#the delimiter part 
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 

        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1 
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length#moving to the next word 
        return res
