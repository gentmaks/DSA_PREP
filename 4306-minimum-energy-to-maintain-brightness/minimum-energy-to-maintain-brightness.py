class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        def merge_interval_score(intervals):
            score = 0
            intervals.sort(key = lambda x: (x[0], -x[1]))
            sorted_ = [intervals[0]]
            for i in range(1, len(intervals)):
                prev_start, prev_end = sorted_[-1]
                start, end = intervals[i]
                if start <= prev_end:
                    sorted_[-1][1] = max(prev_end, end)
                else:
                    sorted_.append(intervals[i])
            for i in sorted_:
                score += (i[1] - i[0] + 1)
            return score

        def find_max_fit(n, brightness):
            return (brightness + 2) // 3

        interval_score = merge_interval_score(intervals)
        max_fit = find_max_fit(n, brightness) 
        return max_fit * interval_score