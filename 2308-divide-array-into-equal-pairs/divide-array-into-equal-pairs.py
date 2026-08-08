class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        for _, v in freq.items():
            if v & 1:
                return False
        return True