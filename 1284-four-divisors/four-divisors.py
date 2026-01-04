class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def numDiv(num):
            count = 0
            total = 0
            for i in range(1, int(num**0.5) + 1): 
                if num % i == 0:
                    print(f"num: {num}, div: {i}")
                    if i * i == num:
                        count += 1
                        total += i
                    else:
                        count += 2
                        total += i
                        total += num / i
            return count, int(total)
        res = 0
        for num in nums:
            count, total = numDiv(num)
            if count == 4:
                res += total
        return res

        