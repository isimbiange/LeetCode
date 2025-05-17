class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [[]] #empty subset

        for num in nums: #looping through the list(subset)
            result += [subset +[num] for  subset in result] #extends the current result by adding a new subset
            #for each existing subset in results create a new subset by adding num

        return result
        