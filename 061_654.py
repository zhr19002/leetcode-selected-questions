class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree2list(root):
    lst = [None] * 15
    if root: 
        lst[0] = root.val
        if root.left: 
            lst[1] = root.left.val
            if root.left.left: 
                lst[3] = root.left.left.val
                if root.left.left.left: 
                    lst[7] = root.left.left.left.val
                if root.left.left.right: 
                    lst[8] = root.left.left.right.val
            if root.left.right: 
                lst[4] = root.left.right.val
                if root.left.right.left: 
                    lst[9] = root.left.right.left.val
                if root.left.right.right: 
                    lst[10] = root.left.right.right.val
        if root.right: 
            lst[2] = root.right.val
            if root.right.left: 
                lst[5] = root.right.left.val
                if root.right.left.left: 
                    lst[11] = root.right.left.left.val
                if root.right.left.right: 
                    lst[12] = root.right.left.right.val
            if root.right.right: 
                lst[6] = root.right.right.val
                if root.right.right.left: 
                    lst[13] = root.right.right.left.val
                if root.right.right.right: 
                    lst[14] = root.right.right.right.val
    else:
        return []
    return lst

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        root = TreeNode(max(nums))
        idx = nums.index(max(nums))
        left = nums[:idx]
        right = nums[(idx + 1):]
        
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        
        return root

s = Solution()
print(tree2list(s.constructMaximumBinaryTree([3,2,1,6,0,5])))