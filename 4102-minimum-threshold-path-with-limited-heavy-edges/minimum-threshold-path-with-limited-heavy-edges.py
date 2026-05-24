class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if not edges:
            if source == target:
                return 0
            return -1
        graph = collections.defaultdict(list)
        for v1, v2, w in edges:
            graph[v1].append((v2, w))
            graph[v2].append((v1, w))
        def can(T):
            dist = [float("inf")] * n
            dist[source] = 0
            q = collections.deque([source])
            while q:
                curr_node = q.popleft()
                for nei, w in graph[curr_node]:
                    cost = (w > T)
                    if dist[curr_node] + cost < dist[nei]:
                        dist[nei] = dist[curr_node] + cost
                        if not cost:
                            q.appendleft(nei)
                        else:
                            q.append(nei)

            return dist[target] <= k

            
        candidate = float("inf")
        max_weight = max(edges, key = lambda x: x[2])[2]
        lo, hi = 0, max_weight
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                candidate = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return candidate if candidate != float("inf") else -1
