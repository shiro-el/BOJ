import sys

def solve():
    input = sys.stdin.readline

    n = int(input())
    C = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    B = sorted(map(int, input().split()), reverse=True)

    if B[0] > C[0]:
        print(-1)
        return

    C.append(0)

    ans = 0
    idx = 0

    for k in range(1, n + 1):
        next_capacity = C[k]
        while idx < m and B[idx] > next_capacity:
            idx += 1

        t = (idx + k - 1) // k
        ans = max(ans, t)

    print(ans)

solve()