class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        labels = list(labels)
        graph = collections.defaultdict(list)
        INF = float("inf")
        for v1, v2, w in edges:
            graph[v1].append((v2, w))
        dist = {(0, 1): 0}
        pq = [(0, 0, 1)]
        heapq.heapify(pq)
        while pq:
            curr_dist, curr_node, curr_streak = heapq.heappop(pq)
            if curr_node == n - 1:
                return curr_dist
            if curr_dist != dist[(curr_node, curr_streak)]:
                continue
            for nei, d in graph[curr_node]:
                new_streak = curr_streak + 1 if labels[nei] == labels[curr_node] else 1
                if new_streak > k:
                    continue
                new_dist = curr_dist + d
                state = (nei, new_streak)
                if new_dist < dist.get(state, INF):
                    dist[state] = new_dist
                    heapq.heappush(pq, (new_dist, nei, new_streak))
        return -1