class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        suffix = []
        for num in reversed(nums):
            if not suffix:
                suffix.append(num)
                continue
            suffix.append(suffix[-1] + num)
        suffix = suffix[::-1]
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > suffix[i+1]/(len(nums) - (i + 1)):
                count += 1
        return count