class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m - 1
        r = n - 1
        for k in range(len(nums1)-1, -1, -1):
            left = nums1[l] if l >= 0 else float("-inf")
            right = nums2[r] if r >= 0 else float("-inf")
            if left > right:
                nums1[k] = left
                l -= 1
            else:
                nums1[k] = right
                r -= 1
        
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        