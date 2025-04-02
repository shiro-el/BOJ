from itertools import product
from collections import deque

n01, n02, n03, n04, n05, n06, n07, n08, n09, n10, n11 = map(int, input().split())
box = [
    [
        [
            [
                [
                    [
                        [
                            [
                                [
                                    [
                                        list(map(int, input().split()))
                                        for _ in range(n02)
                                    ]
                                    for _ in range(n03)
                                ]
                                for _ in range(n04)
                            ]
                            for _ in range(n05)
                        ]
                        for _ in range(n06)
                    ]
                    for _ in range(n07)
                ]
                for _ in range(n08)
            ]
            for _ in range(n09)
        ]
        for _ in range(n10)
    ]
    for _ in range(n11)
]

d01 = [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d02 = [0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d03 = [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d04 = [0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d05 = [0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d06 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d07 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0]
d08 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0]
d09 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0]
d10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0]
d11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]

queue, time = [], 0

for a, b, c, d, e, f, g, h, i, j, k in product(
    range(n11),
    range(n10),
    range(n09),
    range(n08),
    range(n07),
    range(n06),
    range(n05),
    range(n04),
    range(n03),
    range(n02),
    range(n01),
):
    if box[a][b][c][d][e][f][g][h][i][j][k] == 1:
        queue.append((a, b, c, d, e, f, g, h, i, j, k))

while True:
    temp = []

    for a, b, c, d, e, f, g, h, i, j, k in queue:
        for x in range(22):
            A, B, C, D, E, F, G, H, I, J, K = (
                a + d11[x],
                b + d10[x],
                c + d09[x],
                d + d08[x],
                e + d07[x],
                f + d06[x],
                g + d05[x],
                h + d04[x],
                i + d03[x],
                j + d02[x],
                k + d01[x],
            )
            if (
                0 <= A < n11
                and 0 <= B < n10
                and 0 <= C < n09
                and 0 <= D < n08
                and 0 <= E < n07
                and 0 <= F < n06
                and 0 <= G < n05
                and 0 <= H < n04
                and 0 <= I < n03
                and 0 <= J < n02
                and 0 <= K < n01
                and not box[A][B][C][D][E][F][G][H][I][J][K]
            ):
                box[A][B][C][D][E][F][G][H][I][J][K] = 1
                temp.append((A, B, C, D, E, F, G, H, I, J, K))

    if temp:
        queue = temp
        time += 1
    else:
        print(
            time
            if all(
                box[a][b][c][d][e][f][g][h][i][j][k]
                for a in range(n11)
                for b in range(n10)
                for c in range(n09)
                for d in range(n08)
                for e in range(n07)
                for f in range(n06)
                for g in range(n05)
                for h in range(n04)
                for i in range(n03)
                for j in range(n02)
                for k in range(n01)
            )
            else -1
        )
        break