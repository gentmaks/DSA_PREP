class Solution:
    def maxDistance(self, moves: str) -> int:
        count = collections.Counter(moves)
        vertical = abs(count["U"] - count["D"])
        horizontal = abs(count["R"] - count["L"])
        return vertical + horizontal + count["_"]