T = int(input())
for case in range(T):
    S = list(input())
    L = {'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'N':0, 'O':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Z':0}
    
    for i in S:
        L[i] += 1
    
    numbers = [0]*10
    
    numbers[0] = L['Z']
    numbers[1] = L['O'] - L['Z'] - L['W'] - L['U']
    numbers[2] = L['W']
    numbers[3] = L['H'] - L['G']
    numbers[4] = L['U']
    numbers[5] = L['F'] - L['U']
    numbers[6] = L['X']
    numbers[7] = L['S'] - L['X']
    numbers[8] = L['G']
    numbers[9] = L['I'] - L['X'] - L['F'] + L['U'] - L['G']
    
    number = ''
    for i in range(10):
        number += str(i) * numbers[i]
    
    print('Case #{}: {}'.format(case + 1, number))