class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = [event for s, e in intervals for event in [(s, 1), (e, -1)]]
        events.sort(key = lambda x: (x[0], -x[1]))
        running = 0
        max_count = 0
        for _, typ in events:
            running += typ
            max_count = max(max_count, running)
        return max_count

            