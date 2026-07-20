class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        div_graph = collections.defaultdict(list)
        queue = collections.deque()
        visited = set()
        res = []
        def bfs(s, t):
            if s not in div_graph or t not in div_graph:
                return -1.0
            queue.append((s, 1))
            visited.add(s)
            while queue:
                curr_s, curr_val = queue.popleft()
                if curr_s == t:
                    queue.clear()
                    visited.clear()
                    return curr_val
                for nei, other_val in div_graph[curr_s]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, curr_val * other_val))
            queue.clear()
            visited.clear()
            return -1.0
        assert(len(equations) == len(values)) # need these to match for correct input
        for i in range(len(equations)):
            num, den, val = equations[i][0], equations[i][1], values[i]
            div_graph[num].append((den, val))
            div_graph[den].append((num, 1. / val))
        for q in queries:
            source, target = q[0], q[1]
            res.append(bfs(source, target))
        return res