class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        total_cost = 0
        cost = 0
        resources = k
        for num in nums:
            if num <= resources:
                resources -= num
            else:
                mult = math.ceil((num - resources)/k)
                resources += (k * mult)
                resources -= num
                total_cost += (cost * mult) + (mult * (mult + 1) // 2)
                cost += mult
        return total_cost % MOD