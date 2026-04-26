from collections import defaultdict 

class DetectSquares:

    def __init__(self):

        self.count_points = defaultdict(int)



        

    def add(self, point: List[int]) -> None:
        x, y = point 
        self.count_points[(x, y)] += 1
        

    def count(self, point: List[int]) -> int:

        """
        1. we loop through the points
        2. we calc if its a diagonal
        3. x, y   dx, dy
        """

        dx, dy = point

        total_squares = 0

        for p, count in self.count_points.items():

            x, y = p

            if abs(x-dx) == abs(y-dy) and ((x != dx) and (y != dy)):

                corner_one = (dx, y) 
                corner_two = (x, dy)

                total_squares += count * self.count_points.get(corner_one, 0) * self.count_points.get(corner_two, 0)


        return total_squares


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)