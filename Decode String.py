class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for index in range(len(s)):
            if s[index]!= ']':
                stack.append(s[index])
            else:
                substr=digits=''
                while stack and stack[-1] != '[':
                    substr=stack.pop()+substr
                stack.pop()
                while stack and stack[-1].isdigit():
                    digits=stack.pop()+digits
                stack.append(int(digits)*substr)
        return ''.join(stack)
