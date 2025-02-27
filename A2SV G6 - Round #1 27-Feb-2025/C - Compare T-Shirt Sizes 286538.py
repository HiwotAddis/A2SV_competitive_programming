# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t = int(input())  
for _ in range(t):
    a, b = input().split()  
    
    x1, t1 = a.count('X'), a[-1]
    x2, t2 = b.count('X'), b[-1]

    if t1 == t2:  
        if t1 == 'S':  
            print('<' if x1 > x2 else '>' if x1 < x2 else '=')
        elif t1 == 'L':  
            print('>' if x1 > x2 else '<' if x1 < x2 else '=')
        else:  
            print('=')
    else: 
        if t1 == 'S' or (t1 == 'M' and t2 == 'L'):
            print('<')
        else:
            print('>')
