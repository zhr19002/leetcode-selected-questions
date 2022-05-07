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
    def findMode(self, lst):
        root = list2tree(lst)
        pre = None
        count, max_count = 0, 0
        result = []
        
        def searchBST(cur):
            nonlocal pre, count, max_count, result
            if not cur:
                return None
            
            searchBST(cur.left)
            
            if not pre:
                count = 1
            elif pre.val == cur.val:
                count += 1
            else:
                count = 1
            if count == max_count:
                result.append(cur.val)
            if count > max_count:
                max_count = count
                result = [cur.val]
            
            pre = cur    
            searchBST(cur.right)
        
        searchBST(root)
        return result

s = Solution()
print(s.findMode([1,1,2,None,None,2,None]))
print(s.findMode([3,2,3,2,2,None,3]))