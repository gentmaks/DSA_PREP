class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        freq = collections.Counter()
        for num in nums:
            freq[num] += 1
            if freq[num] > k:
                continue
            res.append(num)
        return res
        