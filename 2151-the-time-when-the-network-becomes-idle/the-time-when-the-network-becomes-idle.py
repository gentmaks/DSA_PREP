class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        ans = 0
        graph = collections.defaultdict(list)
        shortest = collections.defaultdict(int)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        q = collections.deque([(0, 0)])
        seen = set()
        while q:
            curr_node, curr_dist = q.popleft()
            shortest[curr_node] = curr_dist
            for nei in graph[curr_node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, curr_dist + 1))
        for i, pat in enumerate(patience):
            if not pat:
                continue
            tot_dist = shortest[i] * 2
            send_bound = tot_dist - 1
            last_send_time = (send_bound // pat) * pat
            ans = max(ans, last_send_time + tot_dist)
        return ans + 1