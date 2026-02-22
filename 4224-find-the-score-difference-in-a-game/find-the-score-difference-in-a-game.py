class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player_1 = 0
        player_2 = 0
        active = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                active = 1 - active
            if (i + 1) % 6 == 0:
                active = 1 - active
            if not active:
                player_1 += nums[i]
            else:
                player_2 += nums[i]
        return player_1 - player_2