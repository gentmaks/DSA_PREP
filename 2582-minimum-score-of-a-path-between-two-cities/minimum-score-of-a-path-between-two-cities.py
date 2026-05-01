class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        INF = 1 << 30
        res = INF
        graph = collections.defaultdict(list)
        for v1, v2, dist in roads:
            graph[v1].append((v2, dist))
            graph[v2].append((v1, dist))
        visited = set()
        q = collections.deque()
        q.append(1)
        visited.add(1)
        while q:
            curr = q.popleft()
            for nei, dist in graph[curr]:
                res = min(res, dist)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return res