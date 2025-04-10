# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    s=list(s)
    for i in range(len(s)):
        if s[i]==s[i].lower():
            s[i]=s[i].upper()
        else:
            s[i]=s[i].lower()
    return ''.join(s)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)