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
    return root

def tree2list(root):
    lst = [None] * 7
    if root: 
        lst[0] = root.val
        if root.left: 
            lst[1] = root.left.val
            if root.left.left: 
                lst[3] = root.left.left.val
            if root.left.right: 
                lst[4] = root.left.right.val
        if root.right: 
            lst[2] = root.right.val
            if root.right.left: 
                lst[5] = root.right.left.val
            if root.right.right: 
                lst[6] = root.right.right.val
    else:
        return []
    return lst

class Solution:
    def mergeTrees(self, lst1, lst2):
        root1 = list2tree(lst1)
        root2 = list2tree(lst2)   
        if not root1:
            return root2
        if not root2:
            return root1
        
        queue = deque([root1, root2])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
                
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        
        return root1

s = Solution()
print(tree2list(s.mergeTrees([1,3,2,5,None,None,None], [2,1,3,None,4,None,7])))