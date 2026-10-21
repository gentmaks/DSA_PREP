class Solution:
    def numOfWays(self, n: int) -> int:
        """
        two types of per row patterns
        x -> 121 
        y -> 123 

        Transitions:
        x -> next row
            3 alternating + 2 different
        y -> next row
            2 alternating + 2 different
        """
        MOD = 10 ** 9 + 7
        x = y = 6
        for i in range(1, n):
            new_x = (3 * x + 2 * y) % MOD
            new_y = (2 * x + 2 * y) % MOD
            x = new_x
            y = new_y
        return (x + y) % MOD