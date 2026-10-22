class Spreadsheet:

    def __init__(self, rows: int):
        self.canvas = collections.defaultdict(lambda: collections.defaultdict(int))

    def setCell(self, cell: str, value: int) -> None:
        col, row = cell[0], cell[1:]
        self.canvas[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = cell[0], cell[1:]
        self.canvas[row][col] = 0
        
    def getValue(self, formula: str) -> int:
        first, second = formula[1:].split("+")
        return self._parse_num(first) + self._parse_num(second)

    def _parse_num(self, cell: str):
        if 65 <= ord(cell[0]) <= 90:
            return self.canvas[cell[1:]][cell[0]]
        return int(cell)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)