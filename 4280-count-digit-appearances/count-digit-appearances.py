class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        total = 0
        def get_count(num, digit):
            count = 0
            while num:
                last = num % 10
                if last == digit:
                    count += 1
                num //= 10
            return count
        for num in nums:
            total += get_count(num, digit)
        return total