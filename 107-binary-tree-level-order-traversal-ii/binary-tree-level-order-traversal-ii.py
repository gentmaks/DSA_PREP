# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        q = collections.deque([root])
        while q:
            curr_level = []
            for _ in range(len(q)):
                curr_node = q.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            levels.append(curr_level)
        return levels[::-1] 