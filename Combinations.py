class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(start,n+1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        res=[]
        backtrack(1,[])
        return res
