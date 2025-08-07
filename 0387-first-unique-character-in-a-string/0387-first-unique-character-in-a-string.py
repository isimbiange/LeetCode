class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s) # create a dictionary
        for index, char in enumerate(s): # loop through the string while keeping tract of keys and values
            if count[char] == 1:#if any of the char appears once before others from left to right
                return index # return its index

        return -1# else if none of the character return -1

        
        
        
        

            
        