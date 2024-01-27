from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root: TreeNode):
    if not root:
        return 0
    
    queue = deque([root])
    result = 0
    while queue:
        for i in range(len(queue)):
            cur = queue.popleft()
            if i == 0:
                result = cur.val
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    
    return result


if __name__ == '__main__':
    #Test data
    root_right_left = TreeNode(5, left=TreeNode(7), right=None)
    root_left = TreeNode(2, left=TreeNode(4), right=None)
    root_right = TreeNode(3, left=root_right_left, right=TreeNode(6))
    root = TreeNode(1, root_left, root_right)
    
    print(findBottomLeftValue(root))