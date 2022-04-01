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
    def connectII(self, lst):
        root = list2tree(lst)
        result = []
        if root == None:
            return result
        queue = deque([root])
        while queue:
            size = len(queue)
            tail = None
            for i in range(size):
                cur = queue.popleft()
                if cur.val != None:
                    result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                if tail:
                    tail.nxt = cur
                tail = cur
                if i == size - 1:
                    result.append(None)
        return result

s = Solution()
print(s.connectII([1,2,3,4,5,6,7]))
print(s.connectII([3,9,20,None,None,15,7]))
print(s.connectII([3,9,20,15,7,None,None]))