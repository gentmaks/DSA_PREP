class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        def dfs(node, p):
            dist = 0
            for nei in graph[node]:
                if nei != p:
                    dist += dfs(nei, node)
            if node and (dist or hasApple[node]):
                dist += 2
            return dist
        return dfs(0, -1)