import itertools
class Solution:
    def minRotations(self, s: str) -> int:
        tally = 0
        s = "0" + s
        for pair in itertools.pairwise(s):
            _from, _to = int(pair[0]), int(pair[1])
            if _from > _to:
                _from, _to = _to, _from
            tally += min((_to - _from), (9 - _to + _from + 1))
        return tally

