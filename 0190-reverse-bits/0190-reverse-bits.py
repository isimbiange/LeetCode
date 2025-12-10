class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0                       # start with an empty result
        for i in range(32):           # process all 32 bits
            bit = (n >> i) & 1        # extract the i-th bit of n
            res = res | (bit << (31 - i))  # place that bit in the reversed position
        return res
 


        #constant time 




# reverse the binary bits and find what those reversed bits number is 













































        
        