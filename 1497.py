from itertools import combinations

def main():
    n, m = map(int, input().split())
    gui = set()
    for _ in range(n):
        temp = 0
        for b in input().split()[1]:
            if b == "Y": temp = temp *2 + 1
            else: temp *= 2
        gui.add(temp)
    
    all = 0
    for i in gui:
        all |= i
    all ^= 2**m-1
    
    for i in range(1, m+1):
        for combs in combinations(gui,i):
            tot = all
            for j in combs:
                tot |= j
            if tot == 2**m-1:
                print(i)
                return
    print(-1)

main()