from sys import stdin
import math

def init(L, node, left, right):
    if left == right:
        tree[node] = L[left]
    else:
        mid = (left + right)//2
        init(L, node*2, left, mid)
        init(L, node*2 + 1, mid+1, right)
        tree[node] = min(tree[node*2], tree[node*2+1])

def update(idx, val, node, left, right):
    if left == right == idx:
        tree[node] = val
    elif idx < left or right < idx:
        return
    else:
        mid = (left + right)//2
        update(idx, val, node*2, left, mid)
        update(idx, val, node*2 + 1, mid + 1, right)
        tree[node] = min(tree[node*2], tree[node*2 + 1])

def query(lidx, ridx, node, left, right):
    if right < lidx or ridx < left:
        return float('inf')
    if lidx <= left and right <= ridx:
        return tree[node]
    mid = (left + right)//2
    return min(query(lidx, ridx, node*2, left, mid), query(lidx, ridx, node*2 + 1, mid + 1, right))

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))

tree = [0]*((pow(2, math.ceil(math.log(n,2))+1)))

init(L, 1, 0, n-1)

m = int(stdin.readline())
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    
    if a == 1:
        update(b-1, c, 1, 0, n-1)
    
    else:
        print(query(b-1, c-1, 1, 0, n-1))