class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = set()

        def _dfs(node: int, comp_info: list) -> None:
            visited.add(node)
            comp_info[0] += 1
            comp_info[1] += len(graph[node])
            for nei in graph[node]:
                if nei not in visited:
                    _dfs(nei, comp_info)

        for node in range(n):
            if node in visited:
                continue
            comp_info = [0, 0]
            _dfs(node, comp_info)
            nodes_c, edge_c = comp_info
            res += (edge_c == (nodes_c * (nodes_c - 1)))
        return res

