class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        flips = []
        n = len(arr)
    
        for target in range(n, 1, -1):
            idx = arr.index(target)
            if idx != target - 1:
                arr = arr[:idx+1][::-1] + arr[idx+1:]
                flips.append(idx+1)
                arr = arr[:target][::-1] + arr[target:]
                flips.append(target)
    
        return flips
