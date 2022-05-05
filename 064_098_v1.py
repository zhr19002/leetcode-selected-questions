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
    def isValidBST(self, lst):
        root = list2tree(lst)
        candidate_list = []
        
        def traverse(root):
            nonlocal candidate_list
            if not root:
                return
            
            traverse(root.left)
            candidate_list.append(root.val)
            traverse(root.right)
        
        def is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True
        
        traverse(root)
        
        return is_sorted(candidate_list)
     
s = Solution()
print(s.isValidBST([4,2,7,1,3,None,None]))
print(s.isValidBST([5,1,4,None,None,3,6]))