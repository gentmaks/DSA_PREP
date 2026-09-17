class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        def kadane(nums1, nums2):
            res = 0
            curr = 0
            for i in range(len(nums1)):
                curr = max(0, curr + nums1[i] - nums2[i])
                res = max(res, curr)
            return res + sum(nums2)
        return max(kadane(nums1, nums2), kadane(nums2, nums1))