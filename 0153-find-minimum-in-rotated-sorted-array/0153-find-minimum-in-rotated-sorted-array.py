class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the current window (l..r) is already sorted,
            # the leftmost element is the smallest.
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            # Calculate the middle index
            m = (l + r) // 2

            # Update res to track the smallest number seen so far
            res = min(res, nums[m])

            # If left part is sorted (nums[l] <= nums[m]),
            # then the smallest value must be in the right half.
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Otherwise, the rotation point (and smallest element)
                # is in the left half.
                r = m - 1

        return res