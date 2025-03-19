# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        ans=[]
        if not root:
            return ans
        queue.append(root)
        while queue:
            l=len(queue)
            
            max_=float('-inf')
            for _ in range(l):
                x=queue.popleft()
                max_=max(max_,x.val)

                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            ans.append(max_)
        return ans
            
            


        