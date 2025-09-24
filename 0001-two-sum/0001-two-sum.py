class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {} # dictionary that stores all the numbers

        for i, num in enumerate(nums): #loop through the list of numbers
            complement = target - num #linear subtract target from the all the numbers if to find compement

            if complement in num_dict: # if the complement exist in the nums list
                return [num_dict[complement], i] #return the index of the number in the list

            num_dict[num] = i
        return none #if the complement not in the list return none

            

        