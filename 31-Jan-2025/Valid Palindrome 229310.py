# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i.isalnum() and i != " ":
                arr.append(i.lower())
        return ''.join(arr)==''.join(arr)[::-1]