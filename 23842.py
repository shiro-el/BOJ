'''
num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
L = ['impossible']*51
for i in range(100):
    for j in range(100):
        if i+j < 100:
            i1 = num[i//10]
            i2 = num[i%10]
            j1 = num[j//10]
            j2 = num[j%10]
            ij1 = num[(i+j)//10]
            ij2 = num[(i+j)%10]
            if i1+i2+j1+j2+ij1+ij2+4 <= 50:
                L[i1+i2+j1+j2+ij1+ij2+4] = "{}+{}={}".format(i, j, i+j)
print(L)
'''
L = ['impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', '17+14=31', '57+14=71', '77+14=91', '77+17=94', '71+10=81', '76+11=87', '81+11=92', '81+10=91', '86+11=97', '91+01=92', '91+00=91', '96+01=97', '97+01=98', '95+02=97', '97+02=99', '98+01=99', '95+00=95', '96+03=99', '99+00=99', '88+02=90', '98+00=98', '88+08=96', '88+00=88', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible', 'impossible']
n = int(input())
print(L[n])