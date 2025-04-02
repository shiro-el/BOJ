a = input()
A = []
num = ""
minus = 1
ans = 0

i = 0
while i < len(a):
    if a[i] == "-":
        minus = -1
        i += 1
    elif a[i] == "+":
        i += 1
    else:
        while i < len(a) and a[i] != "+" and a[i] != "-":
            num = num + a[i]
            i += 1
        ans += minus * int(num)
        num = ""

print(ans)