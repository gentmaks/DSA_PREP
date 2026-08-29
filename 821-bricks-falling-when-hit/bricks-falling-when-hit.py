class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, child: int) -> int:
        if child != self.parents[child]:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]

    def union(self, child1: int, child2: int) -> bool:
        parent1, parent2 = self.find(child1), self.find(child2)
        if parent1 == parent2:
            return False
        if self.size[parent1] > self.size[parent2]:
            self.parents[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parents[parent1] = parent2
            self.size[parent2] += self.size[parent1]
        return True

    def get_size(self, child: int) -> int:
        parent = self.find(child)
        return self.size[parent]
    
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(rows * cols + 1)

        # gathering bricks that are hit
        store = set()
        for r, c in hits:
            if grid[r][c]:
                store.add((r, c)) 
                grid[r][c] = 0

        # calculating stable component sizes in the end
        for r in range(rows):
            for c in range(cols):
                if not r and grid[r][c]:
                    uf.union(c, rows * cols)
                if grid[r][c]:
                    for rr, cc in [(r - 1, c), (r, c - 1)]:
                        if rr < 0 or rr >= rows or cc < 0 or cc >= cols or not grid[rr][cc]:
                            continue
                        uf.union(r * cols + c, rr * cols + cc)

        # calculating falling bricks each hit
        res = []
        prev = uf.get_size(rows * cols)
        for r, c in reversed(hits):
            if (r, c) in store:
                grid[r][c] = 1
                if not r:
                    uf.union(c, rows * cols)
                for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols or not grid[rr][cc]:
                        continue
                    uf.union(r * cols + c, rr * cols + cc)
                size = uf.get_size(rows * cols)
                res.append(max(0, size - prev - 1))
                prev = size
            else:
                res.append(0)
        return res[::-1]