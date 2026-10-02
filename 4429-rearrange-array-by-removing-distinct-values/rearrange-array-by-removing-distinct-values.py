class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq = collections.Counter(nums)
        ans = []
        still = len(freq) > 0
        to_delete = []
        while still:
            tmp_ans = []
            for key in freq:
                freq[key] -= 1
                if not freq[key]:
                    to_delete.append(key)
                tmp_ans.append(key)
            tmp_ans.sort()
            ans.extend(tmp_ans)
            if not freq:
                still = False
            for key_to_delete in to_delete:
                del freq[key_to_delete]
        return ans