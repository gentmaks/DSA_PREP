# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        nodes = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root.val)
            dfs(root.right)
        dfs(root)
        total = 0
        for val in nodes:
            if low <= val <= high:
                total += val
        return total
