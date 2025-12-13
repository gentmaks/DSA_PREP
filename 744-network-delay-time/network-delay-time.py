class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for v1, v2, w in times:
            graph[v1].append((v2, w))
        pq = [(0, k)]
        heapq.heapify(pq)
        seen = set()
        while pq:
            curr_time, curr_node = heapq.heappop(pq)
            seen.add(curr_node)
            if len(seen) == n:
                return curr_time
            for nei, w in graph[curr_node]:
                if nei in seen:
                    continue
                heapq.heappush(pq, (curr_time + w, nei))
        return -1
        