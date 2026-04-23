class Solution:
    def minOperations(self, nums: list[int]) -> int:
        CEIL = 2 * (10 ** 5)
        is_prime = [True] * CEIL
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, isqrt(CEIL) + 1):
            if is_prime[i]:
                for j in range(i * i, CEIL, i):
                    is_prime[j] = False
        total = 0
        for i in range(len(nums)):
            curr = nums[i]
            if i & 1:
                while is_prime[curr]:
                    total += 1
                    curr += 1
                continue
            while not is_prime[curr]:
                total += 1
                curr += 1
        return total
