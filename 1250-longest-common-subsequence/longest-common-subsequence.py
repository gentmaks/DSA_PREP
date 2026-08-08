class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        memo = {}
        def dp(i, j):
            if i == len1 or j == len2:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            res = max(dp(i + 1, j), dp(i, j + 1))
            memo[(i, j)] = res
            return res
        return dp(0, 0)
