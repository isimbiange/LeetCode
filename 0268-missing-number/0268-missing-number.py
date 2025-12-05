class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res


        #exclusive o operator Nums= [3,0,1] i=[0,1,2,3] you take i - nums[i] the same way 5^5 in binary is equal to 0 but when we do 5^5^3 the answer is 3 therefore our output will be 0.
        