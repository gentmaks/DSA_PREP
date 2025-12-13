class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = set()
        lookup = set(wordDict)
        def dp(i):
            if i == len(s):
                return True
            if i in cache:
                return False
            for j in range(20):
                if s[i: i + j + 1] in lookup and dp(i + j + 1):
                    return True
            cache.add(i)
            return False
        return dp(0)
        