# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        i = 0
        levels = []
        while q:
            curr_level = []
            for _ in range(len(q)):
                curr = q.popleft()
                curr_level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if i & 1:
                curr_level = curr_level[::-1]
            levels.append(curr_level)
            i += 1
        return levels