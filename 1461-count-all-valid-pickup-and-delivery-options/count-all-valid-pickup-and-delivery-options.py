class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}
        def dp(pickup, delivery):
            if (pickup + delivery) == 2 * n:
                return 1
            key = (pickup, delivery)
            if key in memo:
                return memo[key]
            _pickup = 0
            _deliver = 0
            if pickup < n:
                _pickup = (n - pickup) * dp(pickup + 1, delivery)
            if delivery < pickup:
                _deliver = (pickup - delivery) * dp(pickup, delivery + 1)
            memo[key] = _pickup + _deliver
            return memo[key]
        return dp(0, 0) % MOD