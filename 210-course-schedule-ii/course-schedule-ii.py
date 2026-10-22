class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for post, pre in prerequisites:
            graph[pre].append(post)
            indegree[post] += 1
        q = collections.deque()
        for course in range(numCourses):
            if not indegree[course]:
                q.append(course)
        ordering = []
        while q:
            curr_course = q.popleft()
            ordering.append(curr_course)
            for nei in graph[curr_course]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
        return ordering if len(ordering) == numCourses else []