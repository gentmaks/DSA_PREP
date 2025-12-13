class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_time(rate):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/rate)
            return hrs
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            if calculate_time(mid) <= h:
                candidate = mid
                r = mid - 1
            else:
                l = mid + 1
        return candidate
        