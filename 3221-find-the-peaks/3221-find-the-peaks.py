class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = [] # a new list that will store the peaks

        for i in range(1,len(mountain) -1): # iterate through the mountains from the second first and last since they are in the middle
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]: #if one of the mountains is greater than the both surrounding mountains
                peaks.append(i) #add its index to the peaks list

        return peaks #return those index of the mountains that were peaks
        

        