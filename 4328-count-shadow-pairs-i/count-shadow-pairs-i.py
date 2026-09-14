class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        stack = []
        tally = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            tally += bisect_left(stack, num)
            stack.append(num)
        return tally