class BusBooking:

    def __init__(self, n: int):
        self.seat_ordered = collections.defaultdict(int) 
        self.seat_unordered = collections.defaultdict(int) 
        self.ordered_running = 0
        self.unordered_running = 0
        self.window = {"A": "B", "D": "C"}

    def toggle(self, seat: str) -> None:
        if self.seat_ordered[seat]:
            self.ordered_running -= self.seat_ordered[seat]
            self.unordered_running -= self.seat_unordered[seat]
            self.seat_ordered[seat] = 0
            self.seat_unordered[seat] = 0
            return
        typ, row = seat[0], seat[1:] 
        if typ in self.window:
            if self.seat_ordered[f"{self.window[typ]}{row}"]:
                self.seat_ordered[seat] = 3
            else:
                self.seat_ordered[seat] = 1
        else:
            self.seat_ordered[seat] = 1
        self.seat_unordered[seat] = 1 
        self.ordered_running += self.seat_ordered[seat]
        self.unordered_running += self.seat_unordered[seat]

    def getTotalTime(self) -> int:
        return self.ordered_running


    def getMinTime(self) -> int:
        return self.unordered_running

# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()