class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        max_reach = [0] * (n + 1)
        for i, area in enumerate(ranges):
            start = max(0, i - area)
            end = min(n, i + area)
            max_reach[start] = max(max_reach[start], end)
        taps = 0
        current_end = 0
        farthest = 0
        for i in range(n + 1):
            if i > current_end:
                return -1
            farthest = max(farthest, max_reach[i])
            if i == current_end and current_end < n:
                if farthest == current_end:
                    return -1
                taps += 1
                current_end = farthest
        return taps