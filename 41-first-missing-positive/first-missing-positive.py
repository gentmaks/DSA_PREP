class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lookup = set(nums)
        for i in range(1, 10 ** 6):
            if i not in lookup:
                return i
        
        