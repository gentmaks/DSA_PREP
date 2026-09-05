class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_memo = {}
        min_memo = {}
        def min_dp(i):
            if not i:
                return nums[0]
            if i in min_memo:
                return min_memo[i]
            min_memo[i] = nums[i] + min(0, min_dp(i-1))
            return min_memo[i]
        def max_dp(i):
            if not i:
                return nums[0]
            if i in max_memo:
                return max_memo[i]
            max_memo[i] = nums[i] + max(0, max_dp(i-1))
            return max_memo[i]
        max_subarray = max(max_dp(i) for i in range(len(nums)))
        min_subarray = min(min_dp(i) for i in range(len(nums)))
        total = sum(nums)
        if total == min_subarray:
            return max_subarray
        return max(max_subarray, total - min_subarray)