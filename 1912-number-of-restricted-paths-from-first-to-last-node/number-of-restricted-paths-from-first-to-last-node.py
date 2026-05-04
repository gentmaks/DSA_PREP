import functools
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        def dijkstra():  # Dijkstra to find shortest distance of paths from node `n` to any other nodes
            minHeap = [(0, n)]  # dist, node
            dist = [float('inf')] * (n + 1)
            dist[n] = 0
            while minHeap:
                d, u = heappop(minHeap)
                if d != dist[u]: continue
                for w, v in graph[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heappush(minHeap, (dist[v], v))
            return dist

        @lru_cache(None)
        def dfs(src):
            if src == n: return 1  # Found a path to reach to destination
            ans = 0
            for _, nei in graph[src]:
                if dist[src] > dist[nei]:
                    ans = (ans + dfs(nei)) % 1000000007
            return ans
        
        dist = dijkstra()
        return dfs(1)
