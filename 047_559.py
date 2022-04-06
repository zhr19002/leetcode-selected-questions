from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.middle = None
        self.right = None

def list2tree(lst):
    root = TreeNode(lst[0])
    root.left = TreeNode(lst[1])
    root.middle = TreeNode(lst[2])
    root.right = TreeNode(lst[3])
    root.left.left = TreeNode(lst[4])
    root.left.right = TreeNode(lst[5])
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
                if cur.middle:
                    queue.append(cur.middle)
                if cur.right:
                    queue.append(cur.right)
        return depth

s = Solution()
print(s.maxDepth([1,3,2,4,5,6]))