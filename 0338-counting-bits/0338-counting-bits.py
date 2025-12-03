class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create a list 'dp' of size (n + 1) filled with 0s
        # dp[i] will store the number of 1 bits for integer i
        dp = [0] * (n + 1)

        # 'offset' represents the most recent power of two
        # For example: 1, 2, 4, 8, 16, ...
        offset = 1

        # Loop through all numbers from 1 to n (inclusive)
        for i in range(1, n + 1):

            # When 'i' reaches the next power of two (like 2, 4, 8, 16...),
            # we update 'offset' to this new power of two
            if offset * 2 == i:
                offset = i

            # DP relation: dynamic programming/ using previous result
            # dp[i] = 1 + dp[i - offset]
            # The '+1' accounts for the new leading 1 bit when crossing into the new power-of-2 range
            dp[i] = 1 + dp[i - offset]

        # Return the dp list which now contains the bit counts for all 0 ≤ i ≤ n
        return dp



        