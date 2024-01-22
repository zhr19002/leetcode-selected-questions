import copy
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Invert a tree using recursive traversal
def preorderInvertTree(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    root.left, root.right = root.right, root.left #Swap nodes
    left = preorderInvertTree(root.left)
    right = preorderInvertTree(root.right)
    
    return [root.val] + left + right

#Invert a tree using level-order traversal
def levelOrderInvertTree(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            cur = queue.popleft()
            level.append(cur.val)
            cur.left, cur.right = cur.right, cur.left #Swap nodes
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        result.append(level)
    
    return result

if __name__ == '__main__':
    #Test data
    root_left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root_right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))
    root_1 = TreeNode(4, root_left, root_right)
    
    #Deep copy should be used
    root_2 = copy.deepcopy(root_1) 
    
    print(preorderInvertTree(root_1))
    print(levelOrderInvertTree(root_2))
