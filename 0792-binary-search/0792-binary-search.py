class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            middle = (l + r)// 2
            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        return -1
        