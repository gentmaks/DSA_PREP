"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []
        for emp in schedule:
            for inter in emp:
                events.append((inter.start, 0))
                events.append((inter.end, 1))
        events.sort(key = lambda x: (x[0], x[1]))
        rest = len(schedule)
        last = float("-inf")
        res = []
        for time, t in events:
            if rest == len(schedule) and last != float("-inf"):
                new_interval = Interval(last, time)
                res.append(new_interval)
            rest += (2 * t) - 1
            last = time
        return res