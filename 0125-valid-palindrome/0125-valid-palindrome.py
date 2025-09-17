class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []# new list for palindrome string

        for char in s:#iterate through the string
            if char.isalnum():# check if char is numeric or alphabet
                filtered.append(char.lower()) # put the char together by making all characters lower characters
        cleaned = "".join(filtered)#remove space 

        return cleaned == cleaned[::-1] #retirn True if the reversed string is equal to the string we were given
        
        