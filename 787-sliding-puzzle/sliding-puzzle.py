class Solution:
    moves = {"123450": 0}
    states = ["123450"]
    adj = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [1, 3, 5],
        [2, 4]
    ]
    for s in states:
        z = s.find("0")
        for a in adj[z]:
            S = list(s)
            S[a], S[z] = S[z], S[a]
            n = "".join(S)
            if n in moves:
                continue
            moves[n] = moves[s] + 1
            states.append(n)

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        return self.moves.get("".join(map(str, chain(*board))), -1)