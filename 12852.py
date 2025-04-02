from collections import deque

n = int(input())
L = [0]*(n+1)
queue = deque([1])

while queue:
    k = queue.popleft()
    if k + 1 == n or 2*k == n or 3*k == n:
        L[n] = k
        break
    if 3*k < n and not L[3*k]:
        queue.append(3*k)
        L[3*k] = k   
    if 2*k < n and not L[2*k]:
        queue.append(2*k)
        L[2*k] = k 
    if k+1 < n and not L[k+1]:
        queue.append(k+1)
        L[k+1] = k

ans = [n]
while ans[-1] != 1:
    bef = ans[-1]
    ans.append(L[bef])

print(len(ans)-1)
print(*ans)