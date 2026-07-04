class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        res = dp0 = dp1 = dpmult = dpdiv = float("-inf")
        for num in nums:
            mult, div = num * k, int(num/k)
            dp1 = max(dp1 + num, dpmult + num, dpdiv + num)
            dpmult = max(dp0 + mult, dpmult + mult, mult)
            dpdiv = max(dp0 + div, dpdiv + div, div)
            dp0 = max(dp0 + num, num)
            res = max(res, dp0, dp1, dpdiv, dpmult)
        return res
