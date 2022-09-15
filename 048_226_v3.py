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

class Solution:
    def invertTree(self, lst):
        root = list2tree(lst)
        result = []
        if root == None:
            return result
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                temp = cur.left
                cur.left = cur.right
                cur.right = temp
                result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.invertTree([4,2,7,1,3,6,9]))
