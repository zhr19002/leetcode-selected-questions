class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Implement preorder traversal using recursion
def preorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    left = preorderTraversal(root.left)
    right = preorderTraversal(root.right)
    
    return [root.val] + left + right

#Implement inorder traversal using recursion
def inorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    left = inorderTraversal(root.left)
    right = inorderTraversal(root.right)
    
    return left + [root.val] + right

#Implement postorder traversal using recursion
def postorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    left = postorderTraversal(root.left)
    right = postorderTraversal(root.right)
    
    return left + right + [root.val]
    
if __name__ == '__main__':
    #Test data
    root_left = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
    root_right = TreeNode(6, left=TreeNode(7), right=TreeNode(8))
    root = TreeNode(5, root_left, root_right)
    
    print(preorderTraversal(root))
    print(inorderTraversal(root))
    print(postorderTraversal(root))