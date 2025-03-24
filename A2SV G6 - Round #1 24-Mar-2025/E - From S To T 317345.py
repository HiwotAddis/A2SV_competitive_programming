# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()

    it=iter(t)
    is_sub=all(char in it for char in s)
    if not is_sub:
        print("NO")
        continue

    flag=True
    for char in set(t):
        if s.count(char)+p.count(char)<t.count(char):
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")
        
