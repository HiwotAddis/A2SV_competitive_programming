class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        f=''.join(l)
        left = 0
        right = len(f)-1
        while left < right:
            if f[left] != f[right]:
                return False
            else:
                left+=1
                right-=1
        return True
