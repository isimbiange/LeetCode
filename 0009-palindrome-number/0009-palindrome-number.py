class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        if s =='':
            return False

        left,right=0 , len(s)-1
        while left < right:

            if s[left]!= s[right]:
                return False

            left += 1
            right -= 1
        return True


    
    
   
           
        