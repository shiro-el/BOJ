import sys

def remove(node):
    if Node[node][1] == []:
        Node[node][2] = False
    else:
        for i in Node[node][1]:
            remove(i)

n = int(input())
Node = list(map(int, sys.stdin.readline().split()))
delete = int(input())

for i in range(n):
    Node[i] = [Node[i], [], True]
for i in range(n):
    if Node[i][0] != -1:
        Node[Node[i][0]][1].append(i)

remove(delete)

leaf = 0
for i in Node:
    if i[2] and i[1] == []:
        leaf += 1
if Node[Node[delete][0]][1] == [delete]:
    leaf += 1
print(leaf)