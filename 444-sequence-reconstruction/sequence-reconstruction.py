class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        values = {i for seq in sequences for i in seq}
        graph = collections.defaultdict(set)
        indegrees = collections.defaultdict(int)
        for s in sequences:
            for i in range(len(s) - 1):
                if s[i+1] not in graph[s[i]]:
                    graph[s[i]].add(s[i+1])
                    indegrees[s[i+1]] += 1
        res = []
        q = collections.deque()
        for num in values:
            if not indegrees[num]:
                q.append(num)
        print(q)
        while q:
            if len(q) != 1:
                print("here")
                return False
            curr = q.popleft()
            res.append(curr)
            for nei in graph[curr]:
                indegrees[nei] -= 1
                if not indegrees[nei]:
                    q.append(nei)
        print(res)
        return res == nums
