class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = collections.defaultdict(list)
        visited = set([id])
        for i in range(len(friends)):
            for friend in friends[i]:
                graph[i].append(friend)
        q = collections.deque([(0, id)])
        vids = collections.Counter()
        while q:
            curr_level, curr_node = q.popleft()
            if curr_level == level:
                for vid in watchedVideos[curr_node]:
                    vids[vid] += 1
            for nei in graph[curr_node]:
                if nei not in visited and curr_level + 1 <= level:
                    visited.add(nei)
                    q.append((curr_level + 1, nei))
        sorted_vids = list(vids.items())
        sorted_vids.sort(key = lambda x: (x[1], x[0]))
        return [vid for (vid, count) in sorted_vids]


        
        