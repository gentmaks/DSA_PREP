class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        q = collections.deque([(0, 0)])
        visited = set([(0, 0)])
        while q:
            first, second = q.popleft()
            print(first, second)
            if first == target or second == target or first + second == target:
                return True
            if (first, y) not in visited:
                q.append((first, y))
                visited.add((first, y))
            if (x, second) not in visited:
                q.append((x, second))
                visited.add((x, second))
            if (0, second) not in visited:
                q.append((0, second))
                visited.add((0, second))
            if (first, 0) not in visited:
                q.append((first, 0))
                visited.add((first, 0))
            if first < x:
                left = x - first
                if left < second:
                    if (x, second - left) not in visited:
                       visited.add((x, second - left)) 
                       q.append((x, second - left))
                else:
                    if (first + second, 0) not in visited:
                       visited.add((first + second, 0)) 
                       q.append((first + second, 0))
            if second < y:
                left = y - second
                if left < first:
                    if (first - left, y) not in visited:
                       visited.add((first - left, y)) 
                       q.append((first - left, y))
                else:
                    if (0, first + second) not in visited:
                       visited.add((0, first + second)) 
                       q.append((0, first + second))
        return False