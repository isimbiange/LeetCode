class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if j == len(strs[i]) or strs[i][j] != strs[0][j]:
                    return strs[0][:j]

        return strs[0]


        