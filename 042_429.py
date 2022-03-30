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