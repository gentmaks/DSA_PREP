class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [((x**2 + y**2)**0.5, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(distances)
        res = []
        while k:
            res.append(points[heapq.heappop(distances)[1]])
            k -= 1
        return res