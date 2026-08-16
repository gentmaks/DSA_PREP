class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for v1, v2, cost, tax in roads:
            graph[v1].append((v2, cost, tax))
            graph[v2].append((v1, cost, tax))
        def getOutgoing(node):
            pq = [(0, node)]
            heapq.heapify(pq)
            dist = [float("inf")] * n
            dist[node] = 0
            while pq:
                curr_dist, curr_node = heapq.heappop(pq)
                if curr_dist != dist[curr_node]:
                    continue
                for nei, add_dist, _ in graph[curr_node]:
                    new_dist = curr_dist + add_dist
                    if new_dist < dist[nei]:
                        heapq.heappush(pq, (new_dist, nei))
                        dist[nei] = new_dist
            return dist
        def getIngoing(node):
            pq = [(0, node)]
            heapq.heapify(pq)
            dist = [float("inf")] * n
            dist[node] = 0
            while pq:
                curr_dist, curr_node = heapq.heappop(pq)
                if curr_dist != dist[curr_node]:
                    continue
                for nei, add_dist, tax in graph[curr_node]:
                    new_dist = curr_dist + (add_dist * tax)
                    if new_dist < dist[nei]:
                        heapq.heappush(pq, (new_dist, nei))
                        dist[nei] = new_dist
            return dist

        res = []
        for i in range(n):
            outgoing = getOutgoing(i)
            ingoing = getIngoing(i)
            best = float("inf")
            for j in range(n):
                out_dist = outgoing[j]
                in_dist = ingoing[j]
                apple_cost = prices[j]
                best = min(best, out_dist + in_dist + apple_cost)
            res.append(best)
        return res