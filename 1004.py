def powDist(x1,y1,x2,y2):
    
    return (x1-x2)**2+(y1-y2)**2

def xor(a,b):

    return (a or b) and not (a and b)


########################################################################################################


testcase=int(input())

for i in range(testcase):

    x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    n = int(input())
    L=[]

    count=0

    for i in range(n):

        L+=[input().split()]

    for i in range(n):

        for j in range(3):

            L[i][j]=int(L[i][j])

    for i in range(n):

        powDist1 = powDist(x1, y1, L[i][0], L[i][1])

        powDist2= powDist(x2, y2, L[i][0], L[i][1])

        if xor(powDist1 < L[i][2]**2, powDist2 < L[i][2]**2):

            count+=1

    print(count)