class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        thresh = len(nums) // 2
        freq = collections.Counter(nums)
        for key, val in freq.items():
            if val == thresh:
                return key
        return -1