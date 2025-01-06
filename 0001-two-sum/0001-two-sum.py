class Solution:
    def twoSum(self, nums:list[int], target:[list])-> list[int]:
        numsMap={}
        n=len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in numsMap:
                return [numsMap[complement],i]
            numsMap[nums[i]]=i
        return[]   