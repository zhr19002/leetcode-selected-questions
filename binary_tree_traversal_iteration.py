class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Implement preorder traversal with iteration
def preorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

#Implement inorder traversal with iteration
def inorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    stack = []
    result = []
    cur = root #Define a pointer
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    
    return result

#Implement postorder traversal with iteration
def postorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result[::-1]
    
if __name__ == '__main__':
    #Test data
    root_left = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
    root_right = TreeNode(6, left=TreeNode(7), right=TreeNode(8))
    root = TreeNode(5, root_left, root_right)
    
    print(preorderTraversal(root))
    print(inorderTraversal(root))
    print(postorderTraversal(root))