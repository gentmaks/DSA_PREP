class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        MOD = (10 ** 9) + 7
        starting_ones = 0
        assert(len(nums1) == len(nums0))
        segs = []
        for ones, zeros in zip(nums1, nums0):
            if not zeros:
                starting_ones += ones
            else:
                segs.append((ones * -1, zeros))
        segs.sort()
        res = ["1"] * starting_ones
        for ones, zeros in segs:
            ones *= -1
            for _ in range(ones):
                res.append("1")
            for _ in range(zeros):
                res.append("0")
        return int("".join(res), 2) % MOD