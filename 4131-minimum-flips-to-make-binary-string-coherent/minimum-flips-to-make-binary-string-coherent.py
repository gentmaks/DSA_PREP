class Solution:
    def minFlips(self, s: str) -> int:
        count = [0, 0]
        for char in s:
            count[int(char)] += 1 
        res = min(count[0], count[1])
        if count[1] > 0:
            res = min(res, count[1] - 1)
        if len(s) >= 2:
            if s[0] == '1' and s[-1] == '1':
                res = min(res, count[1] - 2)
            elif s[0] == '1' or s[-1] == '1':
                res = min(res, count[1])
            else:
                res = min(res, count[1] + 1)
        return res