class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,curr_cand,curr_sum):
            if curr_sum== target:
                res.append(curr_cand[:])
                return
            elif curr_sum>target:
                return
            else:
                for i in range(start,len(candidates)):
                    curr_cand.append(candidates[i])
                    backtrack(i,curr_cand,curr_sum + candidates[i])
                    curr_cand.pop()
        res=[]
        candidates.sort()
        backtrack(0,[],0)
        return res
