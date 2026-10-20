class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        bound = 10 ** 9 + 1
        fib = collections.deque([0, 1, 1])
        running = 2
        while running <= bound:
            if running == n:
                return True
            new = fib[-1] + fib[-2]
            fib.append(new)
            running += new
            running -= fib.popleft()
        return False