class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1

        max_area = 0 
        while l < r:
            w = r - l
            h = min(height[l],height[r]) #we take the shortest height because that means that is where the water stops
            a = w * h
            max_area = max(max_area, a) #it gives either the previous max or the current one if it is bigger

            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        