class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        res = 0
        for i in range(max(0, n-k), n+k+1):
            if not (n & i):
                res += i
        return res