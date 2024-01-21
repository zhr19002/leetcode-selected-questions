from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Implement level-order traversal
def levelOrderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            cur = queue.popleft()
            level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        result.append(level)
    
    return result
    
if __name__ == '__main__':
    #Test data
    root_left = TreeNode(9)
    root_right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    root = TreeNode(3, root_left, root_right)
    
    print(levelOrderTraversal(root))
