class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int: 
        timer = 0
        total = 0
        heapq._heapify_max(happiness)
        while k:
            val = heapq._heappop_max(happiness)
            val -= timer
            if val <= 0:
                break
            k -= 1
            timer += 1
            total += val
        return total