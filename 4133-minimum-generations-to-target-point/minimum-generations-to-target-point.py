class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:

        gen = 0

        def get_new_val(a, b):
            ax, ay, az = a // 100, (a // 10) % 10, a % 10
            bx, by, bz = b // 100, (b // 10) % 10, b % 10

            return ((ax + bx) // 2) * 100 + ((ay + by) // 2) * 10  + ((az + bz) // 2)

        s = set()
        for point in points:
            s.add(point[0] * 100 + point[1] * 10 + point[2])
        t = target[0] * 100 + target[1] * 10 + target[2]
        while t not in s:
            temp = set(s)
            ps = list(s)
            for i in range(len(ps) - 1):
                for j in range(i + 1, len(ps)):
                    new_val = get_new_val(ps[i], ps[j])
                    temp.add(new_val)
            if len(s) == len(temp):
                return -1
            s = temp
            gen += 1
        return gen
