class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(rooms)
        cols = len(rooms[0])
        q = collections.deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if not rooms[r][c]:
                    q.append((0, r, c))
        while q:
            dist, r, c = q.popleft()
            rooms[r][c] = min(rooms[r][c], dist)
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if rooms[new_r][new_c] != INF:
                    continue
                q.append((dist + 1, new_r, new_c))