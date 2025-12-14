class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ans = 0
        for i in range(0, len(row), 2):
            print(i)
            comp = row[i] ^ 1
            if row[i + 1] == comp:
                continue
            ans += 1
            for j in range(i + 1, len(row)):
                if row[j] == comp:
                    row[i+1], row[j] = row[j], row[i + 1]
                    break
        return ans
        