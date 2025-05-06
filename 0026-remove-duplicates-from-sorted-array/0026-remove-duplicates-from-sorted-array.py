class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  # We are given a sorted list, so duplicates will be next to each other.
        l = 1  # Pointer 'l' marks the position where the next unique number should go. Starts at 1 since nums[0] is always unique.
        for r in range(1, len(nums)):  # 'r' scans the list from the second element to the end.
            if nums[r] != nums[r - 1]:  # If current element is different from the previous one, it's unique.
                nums[l] = nums[r]  # Place the unique element at index 'l'
                l += 1  # Move 'l' forward to prepare for the next unique element
        return l  # Return the count of unique elements (and the first l elements of nums are now the unique values)


        