# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=defaultdict(list)
        l=0
        def larg(node,l,arr):
            if node:
                arr[l].append(node.val)
                larg(node.left,l+1,arr)
                larg(node.right,l+1,arr)
        larg(root,l,ans)
        res=[]
        for i in ans.values():
            res.append(max(i))
        return res
            


        