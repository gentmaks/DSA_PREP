class Solution:
    bound = 10 ** 9
    parity = [[], []]
    for i in range(1, 100000):
        s = str(i)
        s_odd = s[:-1] + s[::-1]
        s_even = s + s[::-1]
        v_odd = int(s_odd)
        v_even = int(s_even)
        if v_odd < bound: parity[v_odd & 1].append(v_odd)
        if v_even < bound: parity[v_even & 1].append(v_even)
    parity[0].sort()
    parity[1].sort()
    def minOperations(self, nums: list[int]) -> int:
        tally = 0
        for num in nums:
            space = self.parity[num & 1]
            i = bisect_left(space, num)
            if i >= len(space):
                i = len(space) - 1
            tally += min(abs(num - space[i]), abs(num - space[i - 1])) // 2
        return tally