class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        
        # Handle negative numbers
        if s[0] == '-':
            return False
        
        # Initialize pointers
        left, right = 0, len(s) - 1
        
        # Check if the string is a palindrome
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

    
    
   
           
        