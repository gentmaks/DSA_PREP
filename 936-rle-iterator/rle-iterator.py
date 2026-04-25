class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.curr_idx = 0
        self.curr_left = encoding[self.curr_idx]
        self.curr_number = encoding[self.curr_idx + 1]

    """
    [[[3, 8, 0, 9, 2, 5]]
    [2], [1], [1], [2] 
    """
    def next(self, n: int) -> int:
        while self.curr_idx < len(self.encoding):
            if not self.curr_left:
                self._update()
                continue
            if n > self.curr_left:
                n -= self.curr_left
                self._update()
            else:
                self.curr_left -= n
                return self.curr_number
        return -1

    def _update(self):
        self.curr_idx += 2
        while self.curr_idx < len(self.encoding) and not self.encoding[self.curr_idx]:
            self.curr_idx += 2
        if not self._valid_state():
            return
        self.curr_left = self.encoding[self.curr_idx]
        self.curr_number = self.encoding[self.curr_idx + 1]
    
    def _valid_state(self):
        return self.curr_idx < len(self.encoding)


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)