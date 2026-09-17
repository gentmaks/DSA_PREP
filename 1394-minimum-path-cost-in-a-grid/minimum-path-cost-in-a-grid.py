class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def __str__(self):
        return f"val: {self.val}, neighs: {self.neighbors}\n"

    def __repr__(self):
        return self.__str__()

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        levels = [[] for _ in range(rows)]
        val_to_pos = {
            grid[r][c]: (r, c)
            for r in range(rows)
            for c in range(cols)
        }
        for val in range(len(moveCost)):
            node = Node(val)
            row, _ = val_to_pos[val]
            levels[row].append(node)
            for c, cost in enumerate(moveCost[val]):
                node.neighbors.append((c, cost))
        memo = {}
        def dp(i, col):
            if i == rows - 1:
                return grid[i][col]
            key = (i, col)
            if key in memo:
                return memo[key]
            res = float("inf")
            for node in levels[i]:
                if node.val == grid[i][col]:
                    for dst, cost in node.neighbors:
                        res = min(res, grid[i][col] + cost + dp(i + 1, dst))
            memo[key] = res
            return res
        res = float("inf")
        for c in range(cols):
            res = min(res, dp(0, c))
        return res