class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        count = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                last = s % 10
                if last != x:
                    continue
                first = s
                while first >= 10:
                    first //= 10
                count += (first == last == x)
        return count
