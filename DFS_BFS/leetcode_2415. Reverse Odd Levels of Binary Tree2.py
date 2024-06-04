class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root:optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(arr, level):
            if level % 2:
             n = 2 ** level
            for i in range(n//2):
                arr[i].val, arr[n-i-1].val = arr[n-i-1].val, arr[i].val