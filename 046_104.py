from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def list2tree(lst):
    root = TreeNode(lst[0])
    root.left = TreeNode(lst[1])
    root.right = TreeNode(lst[2])
    root.right.left = TreeNode(lst[5])
    root.right.right = TreeNode(lst[6])
    return root

class Solution:
    def maxDepth(self, lst):
        root = list2tree(lst)
        if root == None:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth

s = Solution()
print(s.maxDepth([3,9,20,None,None,15,7]))
