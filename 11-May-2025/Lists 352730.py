# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    list=[]
    for _ in range(N):
        imp=input().split()
        if imp[0]=='append':
            list.append(int(imp[1]))
        elif imp[0]=='insert':
            list.insert(int(imp[1]),int(imp[2]))
        elif imp[0]=='remove':
            list.remove(int(imp[1]))
        elif imp[0]=='sort':
            list.sort()
        elif imp[0]=='pop':
            list.pop()
        elif imp[0]=='reverse':
            list.reverse()
        elif imp[0]=='print':
            print(list)
    