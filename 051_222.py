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
    root.left.left = TreeNode(lst[3])
    root.left.right = TreeNode(lst[4])
    root.right.left = TreeNode(lst[5])
    return root

class Solution:
    def countNodes(self, lst):
        root = list2tree(lst)
        if root == None:
            return 0
        queue = deque([root])
        result = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                result += 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result

s = Solution()
print(s.countNodes([1,2,3,4,5,6]))