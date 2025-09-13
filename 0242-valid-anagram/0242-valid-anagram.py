#from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):

            return False

        return Counter(s)==Counter(t) # the Counter is a dictionaty that counts how many times characters appears and if the have the same characters from both strings then it return True

        



        