class Solution(object):
    def inorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)          # Left
            result.append(node.val) # Node
            dfs(node.right)         # Right
        
        dfs(root)
        return result
