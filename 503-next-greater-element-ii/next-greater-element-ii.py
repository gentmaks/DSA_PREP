class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * (len(nums))
        mono_stack = []
        for i, num in enumerate(nums):
            while mono_stack and nums[mono_stack[-1]]< num:
                res[mono_stack.pop()] = num
            mono_stack.append(i)  
        for i, num in enumerate(nums):
            while mono_stack and nums[mono_stack[-1]]< num:
                res[mono_stack.pop()] = num
            mono_stack.append(i)  
        return res