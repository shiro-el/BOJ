m, s, x1, x2 = map(int, input().split())
a = ((x1-x2)*pow((s-x1), m-2, m))%m
c = (x1-(a*s))%m
print(a, c)