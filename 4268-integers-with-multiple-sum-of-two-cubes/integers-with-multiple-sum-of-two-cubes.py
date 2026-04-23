class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        limit = int(round(n ** (1/3))) + 1
        
        cubes = [i**3 for i in range(limit)]
        freq = collections.defaultdict(int)

        for i in range(limit):
            for j in range(i + 1, limit):
                curr_sum = cubes[i] + cubes[j]
                if curr_sum > n:
                    break
                freq[curr_sum] += 1

        return sorted([num for num, count in freq.items() if count >= 2])