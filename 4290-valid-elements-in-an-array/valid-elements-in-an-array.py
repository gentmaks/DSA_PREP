class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        res = []
        max_vals = []
        max_vals_other = []
        for num in nums:
            if not max_vals:
                max_vals.append(num)
                continue
            max_vals.append(max(max_vals[-1], num))
        for num in reversed(nums):
            if not max_vals_other:
                max_vals_other.append(num)
                continue
            max_vals_other.append(max(max_vals_other[-1], num))
        max_vals_other = max_vals_other[::-1]
        print(max_vals_other)
        for i in range(len(nums)):
            if not i or i == len(nums) - 1:
                res.append(nums[i])
                continue
            if nums[i] > max_vals[i-1] or nums[i] > max_vals_other[i + 1]:
                res.append(nums[i])
        return res
        