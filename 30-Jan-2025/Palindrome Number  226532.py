# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        ans=0
        while num>0:
            ans=ans*10+num%10
            num=num//10
        return ans==x