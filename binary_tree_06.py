from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Recursive traversal
def maxDepthRecursion(root: TreeNode) -> int:
    if not root:
        return 0
    
    left_depth = maxDepthRecursion(root.left)
    right_depth = maxDepthRecursion(root.right)
    
    return 1 + max(left_depth, right_depth)


#Level-order traversal
def maxDepthLevelOrder(root: TreeNode) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    
    return depth


if __name__ == '__main__':
    #Test data
    root_left = TreeNode(9)
    root_right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    root = TreeNode(3, root_left, root_right)
    
    print(maxDepthRecursion(root))
    print(maxDepthLevelOrder(root))