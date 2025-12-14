class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = collections.defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        track = [float("inf")] * len(quiet)
        res = [float("inf")] * len(quiet)
        @cache
        def dfs(node, i):
            if quiet[node] < track[i]:
                track[i] = quiet[node]
                res[i] = node
            for nei in graph[node]:
                dfs(nei, i)
        for i in range(len(quiet)):
            dfs(i, i)
        return res
        