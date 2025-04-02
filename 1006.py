def fourblock(pointer_x, counter):
    return (counter[pointer_x][0] or\
    counter[pointer_x][1] or\
    counter[pointer_x - 1][0] or\
    counter[pointer_x - 1][1])

T = int(input())
for _ in range(T):
    
    N, W = map(int, input().split())
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))


    check1_1 = [False]*N
    check1_2 = [False]*N
    check2_2 = [False]*N

    for i in range(N):
        if L1[i] + L1[i - 1] <= W:
            check1_1[i] = True
        if L1[i] + L2[i] <= W:
            check1_2[i] = True
        if L2[i] + L2[i - 1] <= W:
            check2_2[i] = True
    '''
    print(check1_1)
    print(check1_2)
    print(check2_2)
    '''
    check1_1 = check1_1 * 2
    check1_2 = check1_2 * 2
    check2_2 = check2_2 * 2

    counter = [[False]*2 for __ in range(N)]
    pointer_x = 0
    pointer_y = 0
    count = 0
    ans = 0

    while count < 2*N:
        ans += 1
        k = False
        for i in range(N):
            for j in range(2):
                if not counter[i][j]:
                    pointer_x = i
                    pointer_y = j
                    k = True
                    break
            if k:
                break

        if not pointer_y:
            right = check1_1[pointer_x + 1]
            left = check1_1[pointer_x]
            right_ = check2_2[pointer_x + 1]
            left_ = check2_2[pointer_x]
        else:
            right = check2_2[pointer_x + 1]
            left = check2_2[pointer_x]
            right_ = check1_1[pointer_x + 1]
            left_ = check1_1[pointer_x]
        down = check1_2[pointer_x]
        rightdown = check1_2[pointer_x + 1]
        leftdown = check1_2[pointer_x - 1]

        if not(right or left or down):
            counter[pointer_x][pointer_y] = True
            count += 1
            #print([pointer_x, pointer_y], 'sol', count)
            continue
            
        else:
            if ((left and left_) or\
                (down and leftdown)) and\
                    not fourblock(pointer_x, counter): # leftdown
                
                counter[pointer_x][0] = True     # sol
                counter[pointer_x][1] = True     # sol_
                counter[pointer_x - 1][0] = True # left
                counter[pointer_x - 1][1] = True # left_

                count += 4
                
                #print([pointer_x, pointer_y], 'leftdown', count)
                
                continue
            
            if ((right and right_) or\
                (down and rightdown) and\
                    fourblock(pointer_x + 1, counter)): # rightdown
                
                counter[pointer_x][0] = True     # sol
                counter[pointer_x][1] = True     # sol_
                counter[pointer_x + 1][0] = True # right
                counter[pointer_x + 1][1] = True # right_

                count += 4
                
                #print([pointer_x, pointer_y], 'rightdown', count)

                continue

            if left\
                and not counter[pointer_x][pointer_y]\
                and not counter[pointer_x - 1][pointer_y]: # left
                
                counter[pointer_x][pointer_y] = True     # sol
                counter[pointer_x - 1][pointer_y] = True # left
                
                count += 2
                
                #print([pointer_x, pointer_y], 'left', count)

                continue
            
            if right\
                and not counter[pointer_x][pointer_y]\
                and not counter[pointer_x + 1][pointer_y]: #right
                
                counter[pointer_x][pointer_y] = True     # sol
                counter[pointer_x + 1][pointer_y] = True # right
                
                count += 2
                
                #print([pointer_x, pointer_y], 'right', count)

                continue

            if down\
                and not counter[pointer_x][0]\
                and not counter[pointer_x][1]: #down               
                
                counter[pointer_x][0] = True # sol
                counter[pointer_x][1] = True # down
                
                count += 2
                
                #print([pointer_x, pointer_y], 'down', count)

                continue

            counter[pointer_x][pointer_y] = True # sol

            
            count += 1
            
            #print([pointer_x, pointer_y], 'sol', count)

    print(ans)