N = int(input())
L = [None] * N
H = [None] * N
R = [None] * N

for i in range(N):
    L[i], H[i], R[i] = map(int, input().split())

height = H[0]
end = R[0]
skyline = [height]
temp_end = []
temp_height = []

for i in range(1, N):
    if height > H[i]:
        skyline.append(H[i])
        if end > R[i]:
            pass
        else:
            end = R[i]
    elif height == H[i]:
        end = max(end, R[i])
    else:
        if R[i] > end:
            pass
    
    