from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nxt = None

def list2tree(lst):
    root = TreeNode(lst[0])
    root.left = TreeNode(lst[1])
    root.right = TreeNode(lst[2])
    root.left.left = TreeNode(lst[3])
    root.left.right = TreeNode(lst[4])
    root.right.left = TreeNode(lst[5])
    root.right.right = TreeNode(lst[6])
    return root

class Solution:
    def connect(self, lst):
        root = list2tree(lst)
        result = []
        if root == None:
            return result
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                if i == size - 1:
                    result.append(None)
                    break
                cur.nxt = queue[0]
        return result

s = Solution()
print(s.connect([1,2,3,4,5,6,7]))