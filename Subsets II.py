class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start,path):
            if path not in res:
                res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        nums.sort()
        res=[]
        backtrack(0,[])
        return res
