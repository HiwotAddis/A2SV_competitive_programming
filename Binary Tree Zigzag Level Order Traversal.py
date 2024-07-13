# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        for i in range(len(ans)):
            if i%2!=0:
                ans[i]=ans[i][::-1]
        return ans
