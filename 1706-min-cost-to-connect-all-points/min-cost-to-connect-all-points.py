import heapq
import collections

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        def man_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = man_dist(points[i], points[j])
                graph[i].append((j, dist))
                graph[j].append((i, dist))
        pq = []
        visited = set()
        heapq.heappush(pq, (0, 0))
        while pq:
            curr_weight, curr_node = heapq.heappop(pq)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            res += curr_weight
            for nei, other_weight in graph[curr_node]:
                if nei not in visited:
                    heapq.heappush(pq, (other_weight, nei))
        return res