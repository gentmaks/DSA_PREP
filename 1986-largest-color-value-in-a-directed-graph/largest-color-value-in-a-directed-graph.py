class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for v1, v2 in edges:
            graph[v1].append(v2)
            indegree[v2] += 1
        q = collections.deque()
        n = len(colors)
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            if not indegree[i]:
                q.append(i)
                dp[i][ord(colors[i]) - ord("a")] = 1
        visited = 0
        max_color_value = 0
        while q:
            curr_node = q.popleft()
            visited += 1
            for nei in graph[curr_node]:
                for c in range(26):
                    dp[nei][c] = max(dp[nei][c], dp[curr_node][c] + (1 if c == ord(colors[nei]) - ord("a") else 0))
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
            max_color_value = max(max_color_value, max(dp[curr_node]))
        return max_color_value if visited == n else -1