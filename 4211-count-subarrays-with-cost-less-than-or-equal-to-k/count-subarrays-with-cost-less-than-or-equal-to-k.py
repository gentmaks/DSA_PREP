class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_q = collections.deque()
        min_q = collections.deque()
        l = 0
        count = 0
        for r, num in enumerate(nums):
            while max_q and nums[max_q[-1]] <= num:
                max_q.pop()
            max_q.append(r)
            while min_q and nums[min_q[-1]] >= num:
                min_q.pop()
            min_q.append(r)
            while min_q and max_q and (nums[max_q[0]] - nums[min_q[0]]) * (r - l + 1) > k:
                l += 1
                if l > max_q[0]:
                    max_q.popleft()
                if l > min_q[0]:
                    min_q.popleft()
            count += (r - l + 1)
        return count