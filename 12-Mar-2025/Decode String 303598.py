# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        res=''
        stack=[]
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr=''
                digit=''
                while stack and stack[-1]!='[':
                    substr=stack.pop()+substr
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit=stack.pop()+digit
                stack.append(int(digit)*substr)
        return ''.join(stack)