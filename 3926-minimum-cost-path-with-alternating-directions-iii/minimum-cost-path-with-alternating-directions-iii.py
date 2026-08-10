class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        dest = (m - 1, n - 1)
        pq = [(1, 0, 0, 1)]          # cost, r, c, next_action_parity (1=odd)
        best = {(0, 0, 1): 1}
        while pq:
            cost, r, c, par = heapq.heappop(pq)
            if (r, c) == dest:
                return cost
            if cost > best.get((r, c, par), float("inf")):
                continue
            legal = [(1, 0), (0, 1)] if par == 1 else [(-1, 0), (0, -1)]
            illegal = [(-1, 0), (0, -1)] if par == 1 else [(1, 0), (0, 1)]
            nxt = 1 - par
            for dr, dc in legal:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nc_cost = cost + (nr + 1) * (nc + 1)
                    if nc_cost < best.get((nr, nc, nxt), float("inf")):
                        best[(nr, nc, nxt)] = nc_cost
                        heapq.heappush(pq, (nc_cost, nr, nc, nxt))
            for dr, dc in illegal:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nc_cost = cost + (nr + 1) * (nc + 1) + penalty[r][c]
                    if nc_cost < best.get((nr, nc, nxt), float("inf")):
                        best[(nr, nc, nxt)] = nc_cost
                        heapq.heappush(pq, (nc_cost, nr, nc, nxt))
            wait_cost = cost + penalty[r][c]
            if wait_cost < best.get((r, c, nxt), float("inf")):
                best[(r, c, nxt)] = wait_cost
                heapq.heappush(pq, (wait_cost, r, c, nxt))
        return -1