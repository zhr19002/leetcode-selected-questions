from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.middle = None
        self.right = None

def list2tree(lst):
    if lst[0] != None: root = TreeNode(lst[0])
    if lst[1] != None: root.left = TreeNode(lst[1])
    if lst[2] != None: root.middle = TreeNode(lst[2])
    if lst[3] != None: root.right = TreeNode(lst[3])
    if lst[4] != None: root.left.left = TreeNode(lst[4])
    if lst[5] != None: root.left.right = TreeNode(lst[5])
    return root

class Solution:
    def levelOrder(self, lst):
        root = list2tree(lst)
        results = []
        if root == None:
            return results
        queue = deque([root])
        while queue:
            result = []
            for i in range(len(queue)):
                cur = queue.popleft()
                result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.middle:
                    queue.append(cur.middle)
                if cur.right:
                    queue.append(cur.right)
            results.append(result)
        return results

s = Solution()
print(s.levelOrder([1,3,2,4,5,6]))
