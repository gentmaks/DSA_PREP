class Solution:
    def countArrangement(self, n: int) -> int:
        """
        n integers (1...n)
        find valid perms
            valid perm -> for each i in range (1, n):
                perm[i] mod i === 0
            or  i mod perm[i] === 0

        so we want to check which subsets of [1...n] have those properties
        for each (idx, number) pair in that collection

        can use bitmasks to more efficiently represent each subset
        only add numbers if condition is met, check which numbers we can add
        when we reach the end of the subset return 1 since all conditions met
        and this is a valid subset
        """
        memo = {}
        def dp(mask, pos):
            if pos > n:
                return 1
            if (mask, pos) in memo:
                return memo[(mask, pos)]
            ans = 0
            for i in range(n):
                num = i + 1
                if not (mask & (1 << i)):
                    if (not num % pos) or (not pos % num):
                        ans += dp(mask | (1 << i), pos + 1)
            memo[(mask, pos)] = ans
            return ans
        return dp(0, 1)