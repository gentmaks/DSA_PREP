class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        banned = set([3, 4, 7])
        changed = set([2, 5, 6, 9])
        for num in range(1, n + 1):
            valid_flag = True
            changed_flag = False
            while num:
                last_digit = num % 10
                if last_digit in banned:
                    valid_flag = False
                elif last_digit in changed:
                    changed_flag = True
                num //= 10
            res += (valid_flag and changed_flag)
        return res