X, Y, D, T = map(int, input().split())
time = 0
distance = (X**2+Y**2)**0.5
if D/T > 1:
    if distance//D != 0:
        time = min(T*(distance//D)+distance % D, T*(distance//D)+T+D-distance%D, T*(distance//D+1))
    else:
        time = min(T*(distance//D)+distance % D, T*(distance//D)+T+D-distance%D, T*(distance//D+2))
    print(time)
else:
    print(distance)