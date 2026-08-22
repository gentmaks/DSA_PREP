class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        total = sum(i for i in range(1, maxChoosableInteger+1))
        if total < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        bound = maxChoosableInteger
        memo = {}
        def dp(mask, tally):
            if tally <= 0:
                return False
            if mask not in memo:
                for i in range(1, bound + 1):
                    if not (mask & (1 << i - 1)):
                        if i >= tally:
                            memo[mask] = True
                            return True
                        else:
                            if not dp(mask | (1 << i - 1), tally - i):
                                memo[mask] = True
                                return True
                            else:
                                memo[mask] = False
            return memo[mask] 
        return dp(0, desiredTotal)