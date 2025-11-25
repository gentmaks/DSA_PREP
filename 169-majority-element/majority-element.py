class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_ele = nums[0]
        maj_count = 1
        for i in range(1, len(nums)):
            if nums[i] != major_ele:
                maj_count -= 1
                if not maj_count:
                    major_ele = nums[i]
                    maj_count = 1
                continue
            maj_count += 1
        return major_ele
        