import sys
sys.setrecursionlimit(10 ** 9)

def preToPost(start, end):
    if start > end:
        return
    
    fin = end + 1
    for i in range(start+1, end+1):
        if Node[start] < Node[i]:
            fin = i
            break
    
    preToPost(start+1, fin-1)
    preToPost(fin, end)
    print(Node[start])

Node = []

count = 0
while count <= 10000:
    try:
        temp = int(input())
    except:
        break
    Node.append(temp)
    count += 1
preToPost(0, len(Node)-1)