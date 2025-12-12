class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        for num in freq:
            if freq[num] > len(nums)//2:
                return num
        