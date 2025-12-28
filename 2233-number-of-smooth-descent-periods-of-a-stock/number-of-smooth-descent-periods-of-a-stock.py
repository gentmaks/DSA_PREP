class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        length = 1
        total = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[r-1] != -1:
                total += (length * (length + 1) // 2) 
                length = 1
            else:
                length += 1
        total += (length * (length + 1) // 2) 
        return total