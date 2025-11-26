class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        left = right = nums[0]
        res = []
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr > right + 1:
                if left == right:
                    res.append(str(left))
                else:
                    res.append(str(left) + "->" + str(right))
                left = right = curr
            else:
                right = curr
        if len(nums) >= 2:
            if nums[-1] == nums[-2] + 1:
                res.append(str(left) + "->" + str(nums[-1]))
            else:
                res.append(str(nums[-1]))
        return res

            

        