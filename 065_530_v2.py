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
    return root

class Solution:
    def getMinDiff(self, lst):
        root = list2tree(lst)
        stack = []
        cur = root
        pre = None
        r = float('inf')
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    r = min(abs(cur.val - pre.val), r)
                pre = cur
                cur = cur.right
        return r
 
s = Solution()
print(s.getMinDiff([1,None,3,None,None,2,None]))
print(s.getMinDiff([8,4,10,1,7,None,15]))