def main():
    n = int(input())
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            a = j-i-1
            b = n-a-2
            res += a*b
    print(res//2)
main()