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
    root.right.right = TreeNode(lst[6])
    return root

class Solution:
    def largestValues(self, lst):
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
                if cur.right:
                    queue.append(cur.right)
            results.append(max(result))
        return results

s = Solution()
print(s.largestValues([1,3,2,5,3,None,9]))