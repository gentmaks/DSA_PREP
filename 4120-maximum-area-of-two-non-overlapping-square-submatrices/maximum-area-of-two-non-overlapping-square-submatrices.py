class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        """
        Approach:
            Check the maximal square side that could be built at top corner (i, j) using 2d dp 
                dp(i, j) with memo = {}
            Helper function to check if two squares of side k can co-exist
            Bin-Search on the grid with k as seperating factor
        """
        rows = len(mat)
        cols = len(mat[0])
        memo = collections.defaultdict(int)
        def dp(i, j):
            if i == rows or j == cols or not mat[i][j]:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1)) + 1
            return memo[(i, j)]
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                dp(r, c)
        def is_poss(k):
            min_r, min_c = sys.maxsize, sys.maxsize
            max_r, max_c = -1, -1
            for r in range(rows):
                for c in range(cols):
                    if memo[(r, c)] >= k:
                        min_r = min(min_r, r)
                        min_c = min(min_c, c)
                        max_r = max(max_r, r)
                        max_c = max(max_c, c)

                        if max_r - min_r >= k or max_c - min_c >= k:
                            return True
            return False

        l, r  = 0, min(rows, cols)
        candidate = 0
        while l <= r:
            k = (l + r) // 2
            if is_poss(k):
                candidate = k
                l = k +1
            else:
                r = k - 1
        return candidate ** 2
