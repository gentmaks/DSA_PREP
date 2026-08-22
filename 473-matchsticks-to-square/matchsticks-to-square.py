class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        side_target = total // 4
        memo = {}
        def dp(mask):
            if mask == (1 << len(matchsticks)) - 1:
                return True
            if mask in memo:
                return memo[mask]
            curr_sum = 0
            for i in range(len(matchsticks)):
                curr_sum += matchsticks[i] if  (mask & (1 << i)) else 0
            curr_sum %= side_target
            for i in range(len(matchsticks)):
                if not (mask & (1 << i)):
                    if curr_sum + matchsticks[i] <= side_target and dp(mask | (1 << i)):
                        memo[mask] = True
                        return True
            memo[mask] = False
            return False
        return dp(0)