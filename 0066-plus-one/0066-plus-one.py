class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the last digit
        for i in range(n - 1, -1, -1):
            digits[i] += 1  # Increment current digit
            
            if digits[i] < 10:  # If no carry, return result
                return digits  
            
            digits[i] = 0  # Carry over, set current digit to 0
        
        # If all digits were 9s, we need to add 1 at the front
        return [1] + digits  


            