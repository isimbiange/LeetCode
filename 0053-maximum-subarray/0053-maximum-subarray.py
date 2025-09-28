class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] #start with the first number in nums as its sum
        #Kadane's algorithm/dynamic programming)
        curr_sum = 0 #equal to 0 until we add other numbers

        for num in nums:
            curr_sum = max(curr_sum + num, num)
            #if curr sum +num is < and num is > you go with the buggest. , means or
            max_sum = max (max_sum, curr_sum)

        return max_sum
        