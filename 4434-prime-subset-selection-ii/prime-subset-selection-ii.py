class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        bound = (n + 1)
        is_prime = [1] * bound
        is_prime[0] = is_prime[1] = 0
        def sieve():
            for i in range(2, (bound // 2) + 1):
                if is_prime[i]:
                    _iter = i + i
                    while _iter < bound:
                        is_prime[_iter] = 0
                        _iter += i
        sieve()
        primes = [i for i in range(len(is_prime)) if is_prime[i]]
        k = len(primes)

        @lru_cache(None)
        def dp(i, rem):
            if i == k:
                return (0, ())
            best = dp(i + 1, rem)
            p = primes[i]
            if p <= rem:
                t_sum, t_arr = dp(i + 1, rem - p)
                cand = (t_sum + p, (p,) + t_arr)
                if (-cand[0], len(cand[1]), cand[1]) < (-best[0], len(best[1]), best[1]):
                    best = cand
            return best
        return list(dp(0, s)[1])   
    