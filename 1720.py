n = int(input())
A = [0,1,3]
for i in range(3,n+1):
    A.append(A[i-1]+2*A[i-2])

if n==1:
    print(1)
elif n==2:
    print(3)
elif n%2==0:
    print((A[n]+A[n//2]+2*A[n//2-1])//2)
else:
    print((A[n]+A[n//2])//2)