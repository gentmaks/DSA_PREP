class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        buckets = collections.defaultdict(int)
        freq = collections.Counter(nums)
        for _, v in freq.items():
            buckets[v] += 1
        for num, count in freq.items():
            if buckets[count] == 1:
                return num
        return -1