def quadfunc(a,b,c):
    return (-b+(b**2-4*a*c)**0.5)/(2*a)

###################################################################

T = int(input())

for i in range(T):
    x, y = input().split()
    dist = int(y) - int(x)
    
    halfuse = quadfunc(1, 1, dist)
    if type(halfuse) == "int":
        use = 2 * halfuse
    else:
        use = 2 * int(halfuse + 1) + 1
    
    print(use)