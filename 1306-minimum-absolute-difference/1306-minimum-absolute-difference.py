class Solution:
    def minimumAbsDifference(self,arr:list[int])->list[list[int]] :
        arr.sort()
        min_diff = float('inf')
        res = []

        for i in range(1,len(arr)):
            curr = arr[i] - arr[i-1]

            if min_diff > curr:
                min_diff = curr 
                res = [[arr[i-1],arr[i]]]
            elif min_diff == curr:
                res.append([arr[i-1],arr[i]])
        return res
            


        
        