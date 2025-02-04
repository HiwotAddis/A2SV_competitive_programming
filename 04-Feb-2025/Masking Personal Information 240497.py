# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s=s.lower()
            s=s.split('@')
            s[0]=s[0][0]+ '*****'+s[0][-1]

            return '@'.join(s)
        else:
            digits=[ch for ch in s if ch.isdigit()]
            local="***-***-{}".format(''.join(digits)[-4:])
            if len(digits)==10:
                return local
            return "+{}-".format('*'*(len(digits)-10))+local