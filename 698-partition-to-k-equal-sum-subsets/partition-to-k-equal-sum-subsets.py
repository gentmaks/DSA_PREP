class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        bucket_target = total / k
        memo = {}
        def dp(mask):
            if mask == (1 << len(nums)) - 1:
                return True
            if mask in memo:
                return memo[mask]
            curr_sum = 0
            for i in range(len(nums)):
                if mask & (1 << i):
                    curr_sum += nums[i]
            curr_sum %= bucket_target
            for i in range(len(nums)):
                if not (mask & (1 << i)):
                    if curr_sum + nums[i] <= bucket_target and dp(mask | (1 << i)):
                        memo[mask] = True
                        return True
            memo[mask] = False
            return memo[mask]
        return dp(0)