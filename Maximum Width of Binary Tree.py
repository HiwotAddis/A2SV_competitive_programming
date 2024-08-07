# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)]) 
        
        while queue:
            level_length = len(queue)
            _, first_pos = queue[0]  
            
            for i in range(level_length):
                node, pos = queue.popleft()
                pos -= first_pos
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
                
                if i == level_length - 1:
                    max_width = max(max_width, pos + 1)
        
        return max_width
