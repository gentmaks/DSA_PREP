class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        maxLength = float("-inf")
        dq = collections.deque()
        l = 0
        total = 0
        final = 0
        for r in range(len(chargeTimes)):
            total += runningCosts[r]
            while dq and chargeTimes[dq[-1]] <= chargeTimes[r]:
                dq.pop()
            dq.append(r)
            res = chargeTimes[dq[0]] + (r - l + 1) * total
            while res > budget:
                total -= runningCosts[l]
                if dq[0] == l:
                    dq.popleft()
                l += 1
                res = chargeTimes[dq[0]] + (r - l + 1) * total if dq else 0
            final = max(final, (r - l + 1))
        return final 