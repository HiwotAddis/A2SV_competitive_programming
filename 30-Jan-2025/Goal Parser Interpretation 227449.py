# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        res=""
        for i in range(len(command)):
            if command[i]=='G':
                res+='G'
            elif command[i]=='(' and command[i+1]==')':
                res+='o'
            elif command[i]=='(' and command[i+1]=='a' :
                res+='al'
        return res