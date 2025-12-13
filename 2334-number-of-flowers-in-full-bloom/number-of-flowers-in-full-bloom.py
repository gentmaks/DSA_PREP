class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        congl = []
        count = 0
        res = [None] * len(people)
        for start, end in flowers:
            congl.append((start, 0, -1))
            congl.append((end, 2, -1))
        for i, p in enumerate(people):
            congl.append((p, 1, i))
        congl.sort(key = lambda x: (x[0], x[1]))
        print(congl)
        for _, ty, idx in congl:
            if ty == 0:
                count += 1
            elif ty == 1:
                res[idx] = count
            elif ty == 2:
                count -= 1
        return res
        