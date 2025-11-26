class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rot_coeff = k % len(nums)
        def reverse_bounds(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse_bounds(0, len(nums) - 1)
        reverse_bounds(0, rot_coeff - 1)
        reverse_bounds(rot_coeff, len(nums) - 1)
        
        """
        Do not return anything, modify nums in-place instead.
        """
        