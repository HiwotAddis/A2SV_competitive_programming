class Solution:
    def longestPalindrome(self, s: str) -> int:
        s=list(s)
        res=0
        c=collections.Counter(s)
        has_odd_frequency = False
        for i in c.values():
            if i%2==0:
                res+=i
            else:
                res+=i-1
                has_odd_frequency = True
        
        return res+1 if has_odd_frequency  else res
        
            
                
