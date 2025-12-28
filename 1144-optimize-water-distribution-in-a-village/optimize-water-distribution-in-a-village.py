class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, cost in enumerate(wells):
            graph[0].append((i + 1, cost))

        for u, v, cost in pipes:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        pq = [(0, 0)] 
        mst = set()
        total = 0

        while pq and len(mst) < n + 1:
            cost, node = heapq.heappop(pq)
            if node in mst:
                continue

            mst.add(node)
            total += cost

            for nei, edge_cost in graph[node]:
                if nei not in mst:
                    heapq.heappush(pq, (edge_cost, nei))

        return total