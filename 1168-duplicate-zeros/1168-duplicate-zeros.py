class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        i = 0 #set the pointer to the first element

        while i < len(arr)-1: #while i is less than the len of the arr
            if arr[i] == 0:# if i is equal to 0
                arr.insert(i+1,0) # insert 0 to the next element space
                del arr[len(arr)-1] #delete the last number in the array
                i=i+2 #move pointer i to i+2 since i +1 has the copied 0
            else:
                i=i+1 #if i wasn't 0 then move the pointer to the next index
        """
        Do not return anything, modify arr in-place instead.
        """
        