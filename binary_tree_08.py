class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root: TreeNode):
    result_1, result_2 = [], []
    path_1, path_2 = [], ''
    if not root:
        return []
    
    traversal_1(root, path_1, result_1)
    traversal_2(root, path_2, result_2)
    
    return result_1, result_2

def traversal_1(root: TreeNode, path_1, result_1):
    path_1.append(root.val)
    if root.left == None and root.right == None:
        result_1.append('->'.join(map(str, path_1)))
        return
    
    if root.left:
        traversal_1(root.left, path_1, result_1)
        path_1.pop()
    if root.right:
        traversal_1(root.right, path_1, result_1)
        path_1.pop()

def traversal_2(root: TreeNode, path_2, result_2):
    path_2 += str(root.val)
    if root.left == None and root.right == None:
        result_2.append(path_2)
        return
    
    if root.left:
        #Simplified version
        #traversal_2(root.left, path_2 + '->', result_2)
        
        #Complete version
        path_2 += '->'
        traversal_2(root.left, path_2, result_2)
        path_2 = path_2[:-2]
        
    if root.right:
        #Simplified version
        #traversal_2(root.right, path_2 + '->', result_2)
        
        #Complete version
        path_2 += '->'
        traversal_2(root.right, path_2, result_2)
        path_2 = path_2[:-2]


if __name__ == '__main__':
    #Test data
    root_left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
    root_right = TreeNode(3, left=TreeNode(6), right=None)
    root = TreeNode(1, root_left, root_right)
    
    print(binaryTreePaths(root))