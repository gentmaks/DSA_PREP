class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n 

    def _find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self._find(self.parents[node])
        return self.parents[node]

    def _union(self, node1, node2):
        node1P, node2P = self._find(node1), self._find(node2)
        if node1P == node2P:
            return False
        if self.size[node1P] > self.size[node2P]:
            self.parents[node2P] = node1P
            self.size[node1P] += self.size[node2P] 
        else:
            self.parents[node1P] = node2P
            self.size[node2P] += self.size[node1P] 
        return True

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = UnionFind(row * col + 2)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        grid = [[0 for _ in range(col)] for _ in range(row)]
        for i, (x, y) in enumerate(cells):
            r, c = x - 1, y - 1
            grid[r][c] = 1
            idx1 = r * col + c + 1
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1:
                    idx2 = new_r * col + new_c + 1
                    dsu._union(idx1, idx2)
            if c == 0:
                dsu._union(0, idx1)
            if c == col - 1:
                dsu._union(row * col + 1, idx1)
            if dsu._find(0) == dsu._find(row * col + 1):
                return i
        return -1