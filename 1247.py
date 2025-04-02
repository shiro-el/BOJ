for _ in range(3):
    n = int(input())
    temp = 0
    for i in range(n):
        temp += int(input())
    if temp > 0:
        print('+')
    elif temp < 0:
        print('-')
    else:
        print(0)