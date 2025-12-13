class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegrees[crs] += 1
        q = collections.deque()
        for i in range(numCourses):
            if not indegrees[i]:
                q.append(i)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in graph[curr]:
                indegrees[nei] -= 1
                if not indegrees[nei]:
                    q.append(nei)
        return res if len(res) == numCourses else []
