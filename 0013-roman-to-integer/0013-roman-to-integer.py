class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} # hash map that stores keys and values
        res = 0 #count result

        for i in range (len(s)):
            if i +1 < len(s) and roman [s[i]] < roman[s[i+1]]: #if i is inside the string and it is gre than the next roman
                res -= roman[s[i]] #subtract i to its next number

            else:
                res += roman[s[i]] # if i is greater than the next number add them

        return res # return the result
        