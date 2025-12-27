class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = numsDivide[0]
        for x in numsDivide:
            g = gcd(x, g)
        def checkDiv(div):
            if not g % div:
                return True
            return False
        heapq.heapify(nums)
        counter = 0
        while nums:
            curr = heapq.heappop(nums)
            print(curr)
            if checkDiv(curr):
                return counter
            counter += 1
        return -1
