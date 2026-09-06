class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 **9 + 7
        valid_cols = []
        tmp_cols = []
        def populate_valid_cols(current):
            """
            backtracking to generate all valid columns combinations
            """
            if len(current) == m:
                valid_cols.append("".join(current))
                return
            for color in "123":
                if current and current[-1] == color:
                    continue
                current.append(color)
                populate_valid_cols(current)
                current.pop()
        populate_valid_cols(tmp_cols)
        @lru_cache(None)
        def dp(col_idx, prev_col):
            """
            counting ways to color from col_idx to the last column,
            given that the previous column coloring is prev_col
            """
            if col_idx == n:
                return 1

            total = 0
            for curr_col in valid_cols:
                for row in range(m):
                    if curr_col[row] == prev_col[row]:
                        break
                else:
                    total += dp(col_idx + 1, curr_col)
            return total
        return dp(0, "0" * m) % MOD