class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        freq = collections.Counter()
        idx = {}
        for i, char in enumerate(s):
            if char in vowels:
                freq[char] += 1
                if char not in idx:
                    idx[char] = i
        vow_bag = []
        for vow, count in freq.items():
            vow_bag.append((vow, count, idx[vow]))
        vow_bag.sort(key = lambda x: (-x[1], x[2]))
        add_vowels = []
        while vow_bag:
            vow_ele = vow_bag.pop()
            for _ in range(vow_ele[1]):
                add_vowels.append(vow_ele[0])
        res = []
        print(add_vowels)
        for char in s:
            if char in vowels:
                res.append(add_vowels.pop())
                continue
            res.append(char)
        return "".join(res)
