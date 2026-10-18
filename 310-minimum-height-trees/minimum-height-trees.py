import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        indegree = [0] * n
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)  # Fix 1
            indegree[v1] += 1
            indegree[v2] += 1
        q = collections.deque(
            i for i in range(n) if indegree[i] == 1
        )
        while q:
            curr_level = list(q)
            for _ in range(len(curr_level)):
                curr = q.popleft()
                for nei in graph[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
            if not q:
                return curr_level
        return []