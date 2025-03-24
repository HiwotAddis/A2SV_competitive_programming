# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t=='+':
                stack.append(int(stack.pop())+ int(stack.pop()))
            elif t=='-':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b)- int(a))
            elif t=='*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif t=='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(int(b)/int(a)))
            else:
                stack.append(t)
            # print(stack)
        return int(stack.pop())