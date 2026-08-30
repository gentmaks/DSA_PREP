class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)

        @lru_cache(maxsize=None)
        def dp(i, j):
            # max distance reachable using first i stations, exactly j stops among them
            if j == 0:
                return startFuel
            if j > i:
                return float('-inf')  # can't make j stops out of i stations

            # option 1: don't use station i-1 as a stop
            best = dp(i - 1, j)

            # option 2: use station i-1 as a stop (only if reachable with j-1 stops so far)
            loc, cap = stations[i - 1]
            reach = dp(i - 1, j - 1)
            if reach >= loc:
                best = max(best, reach + cap)

            return best

        for j in range(n + 1):
            if dp(n, j) >= target:
                return j
        return -1