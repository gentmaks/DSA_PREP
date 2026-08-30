class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {(r, c) for r, c in mines}

        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]

        def dfs(r, c, dr, dc, memo):
            if not (0 <= r < n and 0 <= c < n):
                return 0

            if (r, c) in banned:
                return 0

            if memo[r][c]:
                return memo[r][c]

            memo[r][c] = 1 + dfs(r + dr, c + dc, dr, dc, memo)
            return memo[r][c]

        res = 0

        for r in range(n):
            for c in range(n):
                u = dfs(r, c, -1, 0, up)
                d = dfs(r, c, 1, 0, down)
                l = dfs(r, c, 0, -1, left)
                rr = dfs(r, c, 0, 1, right)

                res = max(res, min(u, d, l, rr))

        return res