# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.bt = root
        self.vals = set()
        def dfs(root, clean):
            if not root:
                return
            root.val = clean
            self.vals.add(clean)
            dfs(root.left, clean * 2 + 1)
            dfs(root.right, clean * 2 + 2)
        dfs(self.bt, 0)

    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)