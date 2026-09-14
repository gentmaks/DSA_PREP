class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        tally = 0
        for _, positions in indices.items():
            if len(positions) < 3:
                continue
            diffs = [(b - a) for a, b in zip(positions, positions[1:])]
            tally += all(x == diffs[0] for x in diffs)
        return tally
