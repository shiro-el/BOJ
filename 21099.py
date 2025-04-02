def xor(A,B):
    a = format(A, 'b')
    b = format(B, 'b')
    
    len_a = len(a)
    len_b = len(b)
    
    if len_a > len_b:
        b = "0"*(len_a - len_b) + b
        leg = len_a
    else:
        a = "0"*(len_b - len_a) + a
        leg = len_b
    
    ans = ""
    
    for i in range(leg):
        if a[i] == b[i]:
            ans += "0"
        else:
            ans += "1"
    
    return int(ans, 10)

#################################################################################

n = int(input())
A = list(map(int, input().split()))
visit = [0]*100000

for i in A:
    visit[i] = 1




'''
Ax xor Ay xor Az = Aw
Ax xor Ay = Az xor Aw 

xor는 교환법칙이 성립한다.
2   3   4   5
010 011 100 101
001 101 000

1001 0110 1010 0101
9    6    10   5

11    12    21    22
01011 01100 10101 10110
00111 00011


'''