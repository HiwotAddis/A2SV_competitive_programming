# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dict_chars=Counter(chars)
        ans=0
        for word in words:
            Flag=True
            dict_w=Counter(word)
            for i in dict_w:
                if dict_w[i]>dict_chars[i]:
                    Flag=False
                    break
            if Flag==False:
                Flag=True
            else:
                ans+=len(word)
        return ans