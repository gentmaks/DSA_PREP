class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        node1P, node2P = self.find(node1), self.find(node2)
        if node1P == node2P:
            return False
        if self.size[node1P] < self.size[node2P]:
            self.parents[node1P] = node2P
            self.size[node2P] += self.size[node1P]
        else:
            self.parents[node2P] = node1P
            self.size[node1P] += self.size[node2P]
        return True

    def findCC(self):
        count = 0
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                count += 1
        return count

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        redundant = 0
        for v1, v2 in connections:
            if not uf.union(v1, v2):
                redundant += 1
        cc = uf.findCC()
        if redundant < cc - 1:
            return -1
        return cc - 1

        