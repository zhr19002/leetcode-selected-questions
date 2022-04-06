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
    def minDepth(self, lst):
        root = list2tree(lst)
        if root == None:
            return 0
        queue = deque([root])
        depth = 1
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left == None and cur.right == None:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        return depth

s = Solution()
print(s.minDepth([3,9,20,None,None,15,7]))