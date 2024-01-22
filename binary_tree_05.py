class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    return compare(root.left, root.right)

def compare(left, right):
    if left == None and right != None:
        return False
    elif left != None and right == None:
        return False
    elif left == None and right == None:
        return True
    elif left.val != right.val:
        return False
    
    outside = compare(left.left, right.right)
    inside = compare(left.right, right.left)
    
    return outside and inside


if __name__ == '__main__':
    #Test data
    root_1_left = TreeNode(2, left=TreeNode(3), right=TreeNode(4))
    root_1_right = TreeNode(2, left=TreeNode(4), right=TreeNode(3))
    root_1 = TreeNode(1, root_1_left, root_1_right)
    
    root_2_left = TreeNode(2, left=None, right=TreeNode(3))
    root_2_right = TreeNode(2, left=None, right=TreeNode(3))
    root_2 = TreeNode(1, root_2_left, root_2_right)
    
    print(isSymmetric(root_1))
    print(isSymmetric(root_2))