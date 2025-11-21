class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 2
        changes = []
        for r in range(2, len(nums)):
            print(f"r: {r, nums[r]}, r - 1: {r - 1, nums[r - 1]}, r - 2: {r - 2, nums[r - 2]}")
            print(f"l: {l}, nums[l]: {nums[l]}")
            if nums[r] == nums[r-1] == nums[r-2]:
                continue
            changes.append((l, nums[r]))
            l += 1
        for l_idx, val in changes:
            nums[l_idx] = val
        return l 


        