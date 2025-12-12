class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        leader = nums[0]
        leader_count = 1     
        for i in range(1, len(nums)):
            if nums[i] != leader:
                leader_count -= 1
                if not leader_count:
                    leader = nums[i]
                    leader_count = 1
            else:
                leader_count += 1
        return leader