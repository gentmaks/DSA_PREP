class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        for num in nums:
            if freq[num] >= 2:
                return True
        return False
        