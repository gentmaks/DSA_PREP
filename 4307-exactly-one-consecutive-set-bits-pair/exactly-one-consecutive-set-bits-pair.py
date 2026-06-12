class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        bin_string = bin(n)
        for i in range(1, len(bin_string)):
            if bin_string[i] == bin_string[i-1] == "1":
                count += 1
        return count == 1
            