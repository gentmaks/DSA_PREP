class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        pq = [(0, start[0], start[1])]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        def isValid(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or maze[r][c] != 0:
                return False
            return True

        def getNextPositions(r, c):
            next_positions = []
            for dr, dc in directions:
                curr_r, curr_c, dist = r, c, 0
                while isValid(curr_r + dr, curr_c + dc):
                    curr_r += dr
                    curr_c += dc
                    dist += 1
                next_positions.append((curr_r, curr_c, dist))
            return next_positions

        while pq:
            dist, curr_r, curr_c = heapq.heappop(pq)
            if (curr_r, curr_c) in visited:
                continue
            if [curr_r, curr_c] == destination:
                return dist
            visited.add((curr_r, curr_c))
            next_positions = getNextPositions(curr_r, curr_c)
            for new_r, new_c, add_dist in next_positions:
                heapq.heappush(pq, (dist + add_dist, new_r, new_c))
        return -1
