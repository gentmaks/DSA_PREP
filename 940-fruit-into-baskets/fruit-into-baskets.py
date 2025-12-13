class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        allowed = {}
        max_length = 0
        for r in range(len(fruits)):
            while fruits[r] not in allowed and len(allowed) >= 2:
                allowed[fruits[l]] -= 1
                if not allowed[fruits[l]]:
                    del(allowed[fruits[l]])
                l += 1
            if fruits[r] in allowed:
                allowed[fruits[r]] += 1
            else:
                allowed[fruits[r]] = 1
            max_length = max(max_length, r - l + 1)
        return max_length
        