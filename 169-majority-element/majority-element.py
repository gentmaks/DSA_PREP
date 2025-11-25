class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(collections.Counter(nums).items(), key = lambda tup: tup[1])[0]
        