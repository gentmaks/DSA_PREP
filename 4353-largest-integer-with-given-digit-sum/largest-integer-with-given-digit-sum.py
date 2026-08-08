class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if not s:
            return 0
        builder = []
        while s:
            if not n:
                return -1
            curr = min(9, s)
            s -= curr
            builder.append(str(curr))
            n -= 1
        builder += ["0"] * n
        return int("".join(builder))
            