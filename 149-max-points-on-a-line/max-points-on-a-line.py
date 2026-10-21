class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        max_count = 0
        INF = float("inf")
        def get_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 - x2 == 0:
                return INF
            return (y1 - y2) / (x1 - x2)
        for i, p in enumerate(points):
            slopes = collections.defaultdict(int)
            for j, other_p in enumerate(points):
                if i == j:
                    continue
                slopes[get_slope(p, other_p)] += 1
                max_count = max(max_count, max(slopes.values()))
        return max_count + 1