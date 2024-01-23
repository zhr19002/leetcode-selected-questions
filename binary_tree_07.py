from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Recursive traversal
def countNodesRecursion(root: TreeNode) -> int:
    if not root:
        return 0
    
    left_num = countNodesRecursion(root.left)
    right_num = countNodesRecursion(root.right)
    
    return 1 + left_num + right_num

#Level-order traversal
def countNodesLevelOrder(root: TreeNode) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    count = 0
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            count += 1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    
    return count


if __name__ == '__main__':
    #Test data
    root_left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
    root_right = TreeNode(3, left=TreeNode(6), right=None)
    root = TreeNode(1, root_left, root_right)
    
    print(countNodesRecursion(root))
    print(countNodesLevelOrder(root))