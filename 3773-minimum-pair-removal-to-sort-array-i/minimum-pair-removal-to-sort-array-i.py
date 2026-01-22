class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        counter = 0
        while True:
            checkCount = 0
            smallestSum = float("inf")
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] < smallestSum:
                    foundIdx = i
                    smallestSum = nums[i] + nums[i+1]
                if nums[i+1] < nums[i]:
                    checkCount += 1
            if not checkCount:
                break
            nums = nums[:foundIdx] + [smallestSum] + nums[foundIdx+2:]
            counter += 1
        return counter