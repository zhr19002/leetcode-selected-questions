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
    def averageOfLevels(self, lst):
        root = list2tree(lst)
        result = []
        if root == None:
            return result
        queue = deque([root])
        while queue:
            size = len(queue)
            sum_ = 0
            for i in range(size):
                cur = queue.popleft()
                sum_ += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(sum_ / size)
        return result

s = Solution()
print(s.averageOfLevels([3,9,20,None,None,15,7]))