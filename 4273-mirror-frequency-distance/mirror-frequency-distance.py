class Solution:
    def mirrorFrequency(self, s: str) -> int:
        res = 0
        lm = {}
        dm = {}
        for i in range(13):
            lm[chr(97 + i)] = chr(97 + 25 - i)
            lm[chr(97 + 25 - i)] = chr(97 + i)
        for i in range(5):
            dm[str(i)] = str(9 - i)
            dm[str(9 - i)] = str(i)
        freq = collections.Counter(s)
        seen = set()
        for char in freq:
            if char in seen:
                continue
            mirror = (dm[char] if char.isdigit() else lm[char])
            seen.add(char)
            seen.add(mirror)
            diff = abs(freq[char] - freq[mirror])
            res += diff
        return res