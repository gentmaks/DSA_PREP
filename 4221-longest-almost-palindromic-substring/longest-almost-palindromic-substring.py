class Solution:
    def almostPalindromic(self, s: str) -> int:
        best = 0
        def expand(i, j, removed):
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                elif not removed:
                    return max(expand(i-1, j, True), expand(i, j + 1, True))
                else:
                    break
            length = (j - i - 1)
            if not removed and (i >= 0 or j < len(s)):
                return length + 1
            return length
        for i in range(len(s)):
            best = max(best, expand(i, i, False), expand(i, i + 1, False))
        return best