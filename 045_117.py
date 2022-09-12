from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nxt = None

def list2tree(lst):
    if lst[0] != None: root = TreeNode(lst[0])  
    if lst[1] != None: root.left = TreeNode(lst[1])
    if lst[2] != None: root.right = TreeNode(lst[2])
    if lst[3] != None: root.left.left = TreeNode(lst[3])
    if lst[4] != None: root.left.right = TreeNode(lst[4])
    if lst[5] != None: root.right.left = TreeNode(lst[5])
    if lst[6] != None: root.right.right = TreeNode(lst[6])
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

if __name__ == '__main__':
    s = Solution()
    print(s.connectII([1,2,3,4,5,6,7]))
    print(s.connectII([3,9,20,None,None,15,7]))
    print(s.connectII([3,9,20,15,7,None,None]))
