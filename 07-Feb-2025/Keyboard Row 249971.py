# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dict={'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
              'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
              'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3
        }
        res=[]
        for word in words:
            flag=True
            for i in range(len(word)-1):
                if dict[word[i].lower()] !=dict[word[i+1].lower()]:
                    flag=False
                    break
            if flag:
                res.append(word)
        return res