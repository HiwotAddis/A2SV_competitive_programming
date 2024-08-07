# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        ans=[]
        if not root:
            return []

        while queue:
            n=len(queue)
            val=[]
            while n:
                n-=1
                
                node=queue.popleft()
                val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(val)
        return ans
