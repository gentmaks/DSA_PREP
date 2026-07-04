class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        res = 0
        while k:
            ele = -heapq.heappop(heap)
            if mul > 0:
                ele *= mul
                res += ele
            else:
                res += ele
            k -= 1
            mul -= 1
        return res