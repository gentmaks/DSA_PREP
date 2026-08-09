class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        graph = collections.defaultdict(list)
        weight = 0
        for n, p in enumerate(parent):
            if n:
                graph[p].append(n)
        def get_height(graph):
            def dfs(node):
                res = 0
                for nei in graph[node]:
                    res = max(res, 1 + dfs(nei))
                return res
            return dfs(0) + 1
        h = get_height(graph)
        q = collections.deque([0])
        depth = 1
        while q:
            for _ in range(len(q)):
                curr_n = q.popleft()
                weight += nums[curr_n] * (h - depth + 1)
                for nei in graph[curr_n]:
                    q.append(nei)
            depth += 1
        return weight