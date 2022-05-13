class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
    def sortedArrayToBST(self, nums):
        return self.traversal(nums, 0, len(nums)-1)
        
    def traversal(self, nums, left, right):
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        mid_root = TreeNode(nums[mid])
        mid_root.left = self.traversal(nums, left, mid-1)
        mid_root.right = self.traversal(nums, mid+1, right)
        
        return mid_root

s = Solution()
print(tree2list(s.sortedArrayToBST([-10,-3,0,5,9])))