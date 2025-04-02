from collections import deque
from sys import stdin
#append pop

def count(bracket):
    n = len(bracket)
    stack = deque()
    for j in range(n//2):
        if bracket[j] != "(":
            ans = 0
            cnt = 0
            
            i = 0
            while i < n-1:
                if bracket[i] == "(":
                    stack.append("(")
                    i += 1
                
                if bracket[i+1] == ")":
                    while bracket[i+1] == ")":
                        cnt += 1
                        stack.append(")")
                        i += 1
                    
                    string = ""
                    print(cnt)
                    print(stack)
                    for k in range(2*cnt):
                        string = stack.pop() + string
                    
                    ans += count(string)
                    print(string)
                    string = ""
                    cnt = 0

            
            return ans
    return 2**(n//2-1)

'''
T = int(stdin.readline())
for _ in range(T):
    A = stdin.readline()
    B = stdin.readline()
    a = count(A)
    b = count(B)
    if a == b:
        print("=")
    elif a > b:
        print(">")
    else:
        print("<")
'''
print(count(stdin.readline()))