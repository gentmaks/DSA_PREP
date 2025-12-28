class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        heapq._heapify_max(capacity)
        boxes = 0
        while capacity:
            curr_cap = heapq._heappop_max(capacity)
            boxes += 1
            total -= curr_cap 
            if total <= 0:
                break
        return boxes