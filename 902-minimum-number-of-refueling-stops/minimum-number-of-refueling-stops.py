class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == 0:
                return startFuel
            if j > i:
                return float('-inf')
            best = dp(i - 1, j)
            loc, cap = stations[i - 1]
            reach = dp(i - 1, j - 1)
            if reach >= loc:
                best = max(best, reach + cap)
            return best
        for j in range(n + 1):
            if dp(n, j) >= target:
                return j
        return -1