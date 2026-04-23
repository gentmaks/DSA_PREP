class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            new_i = i 
            while stack and stack[-1][1] > h:
                last_i, last_h = stack.pop()
                max_area = max(max_area, last_h * (i - last_i))
                new_i = last_i
            stack.append((new_i ,h))
        while stack:
            idx, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area