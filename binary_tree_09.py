class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode):
    if root == None:
        return 0
    
    left_value = 0
    if root.left and root.left.left == None and root.left.right == None:
        left_value = root.left.val
    
    return left_value + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)


if __name__ == '__main__':
    #Test data
    root_left = TreeNode(9, left=None, right=None)
    root_right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    root = TreeNode(3, root_left, root_right)
    
    print(sumOfLeftLeaves(root))