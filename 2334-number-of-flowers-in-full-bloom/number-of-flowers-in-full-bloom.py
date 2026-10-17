class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        lo = min(flowers, key = lambda x: x[0])[0]
        hi = max(flowers, key = lambda x: x[1])[1]
        res = [None] * len(people)
        events = []
        flower_count = 0
        for s, e in flowers:
            heapq.heappush(events, (s, 0))
            heapq.heappush(events, (e, 2))
        for i, p in enumerate(people):
            heapq.heappush(events, (p, 1, i))

        while events:
            _, typ, *idx = heapq.heappop(events)
            if not typ:
                flower_count += 1
            elif typ == 1:
                res[idx[0]] = flower_count
            else:
                flower_count -= 1
        return res
