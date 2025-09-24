class Solution(object):
    def containsDuplicate(self, nums):
        h = set() #hash maps only stores strings and does not allow duplicates

        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)
        return False
        