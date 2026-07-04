class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        def _merge_intervals(intervals):
            merged = []
            intervals.sort()
            for start, end in intervals:
                if not merged:
                    merged.append([start, end])
                else:
                    if start - 1 <= merged[-1][1] or start <= merged[-1][1]:
                        merged[-1][1] = max(end, merged[-1][1])
                    else:
                        merged.append([start, end])
            return merged

        merged = _merge_intervals(occupiedIntervals)
        print(merged)
        res = []
        for start, end in merged:
            """
            For each interval, update the bounds based on allowed conditions
            possible cases:
            interval fully inside disallowed zone --> reject the intervals
            start or end of interval are inside the disallowed zone
            disallowed zone fully inside our current interval
            """
            if start >= freeStart and end <= freeEnd:
                continue
            if start >= freeStart and start <= freeEnd:
                res.append([freeEnd + 1, end])
            elif end <= freeEnd and end >= freeStart:
                res.append([start, freeStart - 1])
            elif start <= freeStart and end >= freeEnd:
                res.append([start, freeStart - 1])
                res.append([freeEnd + 1, end])
            else:
                res.append([start, end])
        return res