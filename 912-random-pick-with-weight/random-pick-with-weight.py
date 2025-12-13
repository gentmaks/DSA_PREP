class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        for weight in w:
            if not self.weights:
                self.weights.append(weight)
                continue
            self.weights.append(self.weights[-1] + weight)
        

    def pickIndex(self) -> int:
        random_n = random.randint(1, self.weights[-1])
        for i in range(len(self.weights)):
            if self.weights[i] >= random_n:
                return i

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()