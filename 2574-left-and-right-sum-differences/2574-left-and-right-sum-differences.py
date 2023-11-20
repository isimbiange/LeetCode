class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rightsum = sum(nums)
        leftsum = 0
        output = []
        
        for i in nums:
            output.append(abs(rightsum-leftsum-i))
            rightsum = rightsum - i
            leftsum = leftsum + i
            
        return output