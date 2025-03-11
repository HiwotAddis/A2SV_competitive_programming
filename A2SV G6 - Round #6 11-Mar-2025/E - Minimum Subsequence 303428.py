# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    temp=0
    zeros=[]
    ones=[]
    ans=[]
    if s[0]=='0':
        temp+=1
        zeros.append(temp)
    else:
        temp+=1
        ones.append(temp)
    ans.append(temp)
    for i in range(1,len(s)):
        if s[i]=='0':
            if ones:
                x=ones.pop()
                zeros.append(x)
                ans.append(x)
            else:
                temp+=1
                zeros.append(temp)
                ans.append(temp)
        else:
            if zeros:
                x=zeros.pop()
                ones.append(x)
                ans.append(x)
            else:
                temp+=1
                ones.append(temp)
                ans.append(temp)
    print(temp)
    print(*ans)