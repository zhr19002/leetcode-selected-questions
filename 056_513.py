from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def list2tree(lst):
    if lst[0] != None: root = TreeNode(lst[0])  
    if lst[1] != None: root.left = TreeNode(lst[1])
    if lst[2] != None: root.right = TreeNode(lst[2])
    if lst[3] != None: root.left.left = TreeNode(lst[3])
    if lst[4] != None: root.left.right = TreeNode(lst[4])
    if lst[5] != None: root.right.left = TreeNode(lst[5])
    if lst[6] != None: root.right.right = TreeNode(lst[6])
    if lst[7] != None: root.left.left.left = TreeNode(lst[7])
    if lst[8] != None: root.left.left.right = TreeNode(lst[8])
    if lst[9] != None: root.left.right.left = TreeNode(lst[9])
    if lst[10] != None: root.left.right.right = TreeNode(lst[10])
    if lst[11] != None: root.right.left.left = TreeNode(lst[11])
    if lst[12] != None: root.right.left.right = TreeNode(lst[12])
    if lst[13] != None: root.right.right.left = TreeNode(lst[13])
    if lst[14] != None: root.right.right.right = TreeNode(lst[14])
    return root

class Solution:
    def findBottomLeftValue(self, lst):
        root = list2tree(lst)
        queue = deque([root])
        result = 0
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                if i == 0:
                    result = queue[i].val 
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right) 
        return result

s = Solution()
print(s.findBottomLeftValue([2,1,3,None,None,None,None,None,None,None,None,None,None,None,None]))
print(s.findBottomLeftValue([1,2,3,4,None,5,6,None,None,None,None,7,None,None,None]))