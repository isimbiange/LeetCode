class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Move left forward until we no longer have all three characters
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - right  # all substrings from left to end are valid
                count[s[left]] -= 1
                left += 1

        return res
