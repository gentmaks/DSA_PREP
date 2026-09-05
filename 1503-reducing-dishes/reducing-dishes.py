class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        size = len(satisfaction)
        memo = {}
        def dp(i, picked):
            if i == size:
                return 0
            key = (i, picked)
            if key in memo:
                return memo[key]
            _pick = (picked * satisfaction[i]) + dp(i + 1, picked + 1)
            _skip = dp(i + 1, picked)
            res = max(_pick, _skip)
            memo[key] = res
            return res
        return dp(0, 1)