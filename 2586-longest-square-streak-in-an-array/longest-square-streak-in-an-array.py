class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        streak_map = {}
        nums.sort()
        res = -1
        for num in nums:
            _sqrt = math.sqrt(num)
            if _sqrt * _sqrt == num and _sqrt in streak_map:
                streak_map[num] = streak_map[_sqrt] + 1
                res = max(res, streak_map[num])
            else:
                streak_map[num] = 1
        return res