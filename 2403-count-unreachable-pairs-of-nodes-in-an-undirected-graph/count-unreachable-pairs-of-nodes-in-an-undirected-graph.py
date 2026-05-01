class DSU:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [i for i in range(self.n)]
        self.size = [1 for i in range(self.n)]

    def find(self, child: int) -> int:
        if self.parents[child] != child:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]

    def union(self, node1: int, node2: int) -> bool:
        node1P, node2P = self.find(node1), self.find(node2)
        if node1P == node2P:
            return False
        if self.size[node2P] > self.size[node1P]:
            self.parents[node1P] = node2P
            self.size[node2P] += self.size[node1P]
        else:
            self.parents[node2P] = node1P
            self.size[node1P] += self.size[node2P]
        return True

    def get_size(self, parent: int) -> int:
        return self.size[parent]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        uf = DSU(n)
        for v1, v2 in edges:
            uf.union(v1, v2)
        for i in range(n):
            parent = uf.find(i)
            comp_size = uf.get_size(parent)
            res += (n - comp_size)
        return res//2

